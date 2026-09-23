import PostmortemCard from "@/components/PostmortemCard";
import { getPublicProfile } from "@/lib/api";
import { notFound } from "next/navigation";

export default async function ProfilePage({ params }: { params: { username: string } }) {
  let data;
  try {
    data = await getPublicProfile(params.username);
  } catch {
    notFound();
  }

  const { user, postmortems } = data;

  return (
    <div className="space-y-6">
      <header className="space-y-1">
        <h1 className="text-2xl font-bold text-gray-100">{user.username}</h1>
        <p className="text-sm text-gray-500">{postmortems.length} public postmortem(s)</p>
      </header>

      <div className="grid gap-4 sm:grid-cols-2">
        {postmortems.map((pm: any) => (
          <PostmortemCard key={pm.id} postmortem={pm} />
        ))}
      </div>
    </div>
  );
}

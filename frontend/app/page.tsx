import PostmortemCard from "@/components/PostmortemCard";
import { listPublicPostmortems } from "@/lib/api";

export default async function HomePage() {
  let postmortems = [];
  try {
    postmortems = await listPublicPostmortems();
  } catch {
    postmortems = [];
  }

  return (
    <div className="space-y-8">
      <section className="space-y-3 py-8 text-center">
        <h1 className="text-3xl font-bold text-gray-100">
          Proof over claims. <span className="text-accent">Real bugs, real fixes.</span>
        </h1>
        <p className="mx-auto max-w-xl text-gray-400">
          A searchable archive of Git-backed root cause analyses — the debugging
          depth a resume can&apos;t show.
        </p>
      </section>

      <section className="grid gap-4 sm:grid-cols-2">
        {postmortems.length === 0 && (
          <p className="col-span-2 text-center text-gray-500">
            No public postmortems yet. Sign in and publish your first one.
          </p>
        )}
        {postmortems.map((pm: any) => (
          <PostmortemCard key={pm.id} postmortem={pm} />
        ))}
      </section>
    </div>
  );
}

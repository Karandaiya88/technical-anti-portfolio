export default function LoginPage() {
  const apiUrl = process.env.NEXT_PUBLIC_API_URL;

  return (
    <div className="flex flex-col items-center gap-4 py-20 text-center">
      <h1 className="text-2xl font-bold text-gray-100">Sign in to publish your postmortems</h1>
      <p className="max-w-sm text-gray-400">
        We use GitHub OAuth to fetch commit diffs from repos you choose. We never write to your repos.
      </p>
      <a
        href={`${apiUrl}/auth/github/login`}
        className="rounded-md bg-accent px-5 py-2.5 font-medium text-bg hover:opacity-90"
      >
        Continue with GitHub
      </a>
    </div>
  );
}

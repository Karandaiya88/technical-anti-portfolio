import Link from "next/link";

export default function Navbar() {
  return (
    <header className="border-b border-white/10 bg-panel/60 backdrop-blur">
      <div className="mx-auto flex max-w-5xl items-center justify-between px-4 py-4">
        <Link href="/" className="font-mono text-lg font-semibold text-accent">
          🔬 anti-portfolio
        </Link>
        <nav className="flex gap-6 text-sm text-gray-300">
          <Link href="/dashboard" className="hover:text-accent">Dashboard</Link>
          <a
            href={`${process.env.NEXT_PUBLIC_API_URL}/auth/github/login`}
            className="rounded-md bg-accent px-3 py-1.5 font-medium text-bg hover:opacity-90"
          >
            Sign in with GitHub
          </a>
        </nav>
      </div>
    </header>
  );
}

"use client";

import { useEffect, useState } from "react";
import { useSearchParams } from "next/navigation";
import { listRepos, createPostmortem } from "@/lib/api";

export default function DashboardPage() {
  const searchParams = useSearchParams();
  const [token, setToken] = useState<string | null>(null);
  const [repos, setRepos] = useState<any[]>([]);
  const [form, setForm] = useState({
    title: "",
    hypothesis: "",
    breaking_point: "",
    architectural_rule: "",
    tags: "",
  });
  const [status, setStatus] = useState<string | null>(null);

  useEffect(() => {
    const t = searchParams.get("token") ?? localStorage.getItem("session_token");
    if (t) {
      setToken(t);
      localStorage.setItem("session_token", t);
      listRepos(t).then(setRepos).catch(() => setRepos([]));
    }
  }, [searchParams]);

  if (!token) {
    return (
      <div className="py-20 text-center text-gray-400">
        Please <a href="/login" className="text-accent underline">sign in</a> to access your dashboard.
      </div>
    );
  }

  async function handleSubmit(e: React.FormEvent) {
    e.preventDefault();
    setStatus("Saving...");
    try {
      await createPostmortem(token!, {
        ...form,
        is_public: true,
        tags: form.tags.split(",").map((t) => t.trim()).filter(Boolean),
        diff_snippets: [],
      });
      setStatus("Postmortem saved ✅");
      setForm({ title: "", hypothesis: "", breaking_point: "", architectural_rule: "", tags: "" });
    } catch {
      setStatus("Failed to save ❌");
    }
  }

  return (
    <div className="space-y-10">
      <section>
        <h2 className="mb-3 text-lg font-semibold text-gray-100">Your Repositories</h2>
        <ul className="space-y-1 text-sm text-gray-400">
          {repos.map((r) => (
            <li key={r.id} className="font-mono">{r.full_name}</li>
          ))}
          {repos.length === 0 && <li>No repos loaded yet.</li>}
        </ul>
      </section>

      <section>
        <h2 className="mb-3 text-lg font-semibold text-gray-100">New Postmortem</h2>
        <form onSubmit={handleSubmit} className="card space-y-4">
          <input
            className="w-full rounded-md bg-black/30 px-3 py-2 text-sm outline-none"
            placeholder="Title"
            value={form.title}
            onChange={(e) => setForm({ ...form, title: e.target.value })}
            required
          />
          <textarea
            className="w-full rounded-md bg-black/30 px-3 py-2 text-sm outline-none"
            placeholder="Hypothesis — what did you initially think was wrong?"
            value={form.hypothesis}
            onChange={(e) => setForm({ ...form, hypothesis: e.target.value })}
            rows={3}
          />
          <textarea
            className="w-full rounded-md bg-black/30 px-3 py-2 text-sm outline-none"
            placeholder="Breaking point — what actually failed, and why?"
            value={form.breaking_point}
            onChange={(e) => setForm({ ...form, breaking_point: e.target.value })}
            rows={3}
          />
          <textarea
            className="w-full rounded-md bg-black/30 px-3 py-2 text-sm outline-none"
            placeholder="Architectural rule — the lesson you're keeping"
            value={form.architectural_rule}
            onChange={(e) => setForm({ ...form, architectural_rule: e.target.value })}
            rows={2}
          />
          <input
            className="w-full rounded-md bg-black/30 px-3 py-2 text-sm outline-none"
            placeholder="Tags (comma-separated, e.g. #RaceCondition, #Postgres)"
            value={form.tags}
            onChange={(e) => setForm({ ...form, tags: e.target.value })}
          />
          <button className="rounded-md bg-accent px-4 py-2 font-medium text-bg hover:opacity-90">
            Publish Postmortem
          </button>
          {status && <p className="text-sm text-gray-400">{status}</p>}
        </form>
      </section>
    </div>
  );
}

const API_URL = process.env.NEXT_PUBLIC_API_URL;

function authHeaders(token?: string) {
  return token ? { Authorization: `Bearer ${token}` } : {};
}

export async function listPublicPostmortems(tag?: string) {
  const url = new URL(`${API_URL}/postmortems`);
  if (tag) url.searchParams.set("tag", tag);
  const res = await fetch(url.toString(), { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to load postmortems");
  return res.json();
}

export async function getPublicProfile(username: string) {
  const res = await fetch(`${API_URL}/u/${username}`, { cache: "no-store" });
  if (!res.ok) throw new Error("Profile not found");
  return res.json();
}

export async function listTags() {
  const res = await fetch(`${API_URL}/tags`, { cache: "no-store" });
  if (!res.ok) throw new Error("Failed to load tags");
  return res.json();
}

export async function listRepos(token: string) {
  const res = await fetch(`${API_URL}/repos`, { headers: authHeaders(token) });
  if (!res.ok) throw new Error("Failed to load repos");
  return res.json();
}

export async function createPostmortem(token: string, payload: unknown) {
  const res = await fetch(`${API_URL}/postmortems`, {
    method: "POST",
    headers: { "Content-Type": "application/json", ...authHeaders(token) },
    body: JSON.stringify(payload),
  });
  if (!res.ok) throw new Error("Failed to create postmortem");
  return res.json();
}

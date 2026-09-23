type Tag = { id: string; name: string; category?: string };

type Postmortem = {
  id: string;
  title: string;
  hypothesis?: string;
  breaking_point?: string;
  architectural_rule?: string;
  tags: Tag[];
  created_at: string;
};

export default function PostmortemCard({ postmortem }: { postmortem: Postmortem }) {
  return (
    <div className="card space-y-3">
      <div className="flex items-start justify-between">
        <h3 className="text-lg font-semibold text-gray-100">{postmortem.title}</h3>
        <span className="text-xs text-gray-500">
          {new Date(postmortem.created_at).toLocaleDateString()}
        </span>
      </div>

      {postmortem.architectural_rule && (
        <p className="text-sm italic text-accent">
          Rule learned: {postmortem.architectural_rule}
        </p>
      )}

      {postmortem.breaking_point && (
        <p className="text-sm text-gray-300 line-clamp-3">{postmortem.breaking_point}</p>
      )}

      <div className="flex flex-wrap gap-2 pt-1">
        {postmortem.tags.map((tag) => (
          <span key={tag.id} className="tag-chip">{tag.name}</span>
        ))}
      </div>
    </div>
  );
}

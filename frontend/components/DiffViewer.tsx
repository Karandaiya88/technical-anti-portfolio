"use client";

import ReactDiffViewer from "react-diff-viewer-continued";

type Props = {
  filePath: string;
  faultyChunk: string;
  resolvedChunk: string;
};

/**
 * Renders a sanitized code diff. The backend has already stripped/escaped
 * this content (see backend/app/utils/sanitize.py) — this component only
 * handles presentation, never executes anything from `faultyChunk` /
 * `resolvedChunk`.
 */
export default function DiffViewer({ filePath, faultyChunk, resolvedChunk }: Props) {
  return (
    <div className="card overflow-hidden p-0">
      <div className="border-b border-white/10 bg-black/20 px-4 py-2 font-mono text-xs text-gray-400">
        {filePath}
      </div>
      <ReactDiffViewer
        oldValue={faultyChunk}
        newValue={resolvedChunk}
        splitView={true}
        useDarkTheme={true}
        leftTitle="❌ Faulty"
        rightTitle="✅ Resolved"
      />
    </div>
  );
}

import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{js,ts,jsx,tsx,mdx}", "./components/**/*.{js,ts,jsx,tsx,mdx}"],
  theme: {
    extend: {
      colors: {
        bg: "#0b0f14",
        panel: "#131922",
        accent: "#22d3ee",
        danger: "#f87171",
        success: "#34d399",
      },
    },
  },
  plugins: [],
};
export default config;

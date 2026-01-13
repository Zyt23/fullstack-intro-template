import React, { useEffect, useState } from "react";

type Profile = { name: string; title: string; bio: string };

export default function App() {
  const [profile, setProfile] = useState<Profile | null>(null);

  useEffect(() => {
    fetch("/api/profile")
      .then((r) => r.json())
      .then(setProfile);
  }, []);

  if (!profile) return <div style={{ padding: 24 }}>Loading...</div>;

  return (
    <div style={{ maxWidth: 720, margin: "40px auto", padding: 24, fontFamily: "system-ui" }}>
      <h1 style={{ marginBottom: 8 }}>{profile.name}</h1>
      <div style={{ opacity: 0.7, marginBottom: 16 }}>{profile.title}</div>
      <p style={{ lineHeight: 1.6 }}>{profile.bio}</p>

      <hr style={{ margin: "24px 0" }} />

      <h3>Try editing (PUT /api/profile)</h3>
      <button
        onClick={async () => {
          const next = { ...profile, bio: profile.bio + " ✨" };
          await fetch("/api/profile", {
            method: "PUT",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(next)
          });
          setProfile(next);
        }}
      >
        Add sparkle
      </button>
    </div>
  );
}

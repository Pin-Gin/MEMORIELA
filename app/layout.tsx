import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "MEMORIELA | Official Website",
  description: "AIキャラクター／人格システムを開発するMEMORIELAの公式サイト。Project YURAを中心に、技術・ビジュアル・制作過程を公開しています。",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return (
    <html lang="ja">
      <body>{children}</body>
    </html>
  );
}

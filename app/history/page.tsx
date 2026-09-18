const developmentHistory = [
  { date: "2026.09.11", title: "ゆらの公式ビジュアルを正式決定", text: "久遠ゆらの公式ビジュアルを確定。" },
  { date: "2026.09.06", title: "チャットUI実装", text: "専用Desktop会話UI、画像入力・認識、Relationship永続管理、音声基盤更新を実装。" },
  { date: "2026.08.30", title: "ゆらの人格・自発性を強化", text: "ゆら自身の人格や状態を会話に反映する仕組みを拡張。自分から話しかける機能、Web検索、眠気による状態変化を実装。" },
  { date: "2026.08.23", title: "記憶と感情の仕組みを実装", text: "長期記憶、Relationship、複合感情、音声表現の基盤を実装。" },
  { date: "2026.08.16", title: "久遠ゆら、誕生", text: "Project YURA始動。AIとしての会話・音声機能の最初の基盤を実装。" },
];

export default function HistoryPage() {
  return (
    <main className="subpage">
      <header className="subpageHeader">
        <a className="wordmark" href="/">MEMORIELA - Project.YURA</a>
        <nav aria-label="Main navigation">
          <a href="/about">About</a>
          <a href="/technology">Technology</a>
          <a href="/gallery">Gallery</a>
          <a href="/news">News</a>
          <a href="/contact">Contact</a>
        </nav>
      </header>

      <section className="subpageHero center">
        <span>PROJECT.YURA</span>
        <h1>Development History</h1>
        <p>開発履歴</p>
      </section>

      <section className="subpageContent">
        <div className="timeline">
          {developmentHistory.map((item) => (
            <article key={item.date}>
              <time>{item.date}</time>
              <i />
              <div><h3>{item.title}</h3><p>{item.text}</p></div>
            </article>
          ))}
        </div>
      </section>
    </main>
  );
}

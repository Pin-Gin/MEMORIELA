const xUrl = "https://x.com/MEMORIELA_JP";

const developmentHistory = [
  { date: "2026.09.11", title: "ゆらの公式ビジュアルを正式決定", text: "久遠ゆらの公式ビジュアルを確定。" },
  { date: "2026.09.06", title: "チャットUI実装", text: "専用Desktop会話UI、画像入力・認識、Relationship永続管理、音声基盤更新を実装。" },
  { date: "2026.08.30", title: "ゆらの人格・自発性を強化", text: "ゆら自身の人格や状態を会話に反映する仕組みを拡張。自分から話しかける機能、Web検索、眠気による状態変化を実装。" },
  { date: "2026.08.23", title: "記憶と感情の仕組みを実装", text: "長期記憶、Relationship、複合感情、音声表現の基盤を実装。" },
  { date: "2026.08.16", title: "久遠ゆら、誕生", text: "Project YURA始動。AIとしての会話・音声機能の最初の基盤を実装。" },
];

export default function Home() {
  return (
    <main>
      <section className="hero" id="home">
        <header className="heroHeader">
          <a className="wordmark" href="/">MEMORIELA - Project.YURA.</a>
          <nav aria-label="Main navigation">
            <a href="/">Home</a>
            <a href="/about">About</a>
            <a href="/technology">Technology</a>
            <a href="/gallery">Gallery</a>
            <a href="/#history">Development History</a>
          </nav>
          <div className="heroActions"><span>開発局</span><b>☰</b></div>
        </header>

        <div className="heroLeftCopy">
          <p>AIと。<br/>生きる。<br/>創る。<br/>そして、<br/>あなたと歩む。</p>
          <small>MEMORIELA<br/>Project.YURA</small>
        </div>

        <div className="heroBottom">
          <span># Project.YURA　｜　# 開発局　｜　# AI × Creativity</span>
          <b>SCROLL</b>
          <span>いつかじゃない、いま、ここから。</span>
        </div>
      </section>

      <section className="history section" id="history">
        <div className="sectionHead center">
          <span>PROJECT.YURA</span>
          <h2>Development History</h2>
          <p>開発履歴</p>
        </div>
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

      <footer>
        <div><strong>MEMORIELA</strong><span>Project.YURA</span></div>
        <nav>
          <a href="/">Home</a>
          <a href="/about">About</a>
          <a href="/technology">Technology</a>
          <a href="/gallery">Gallery</a>
          <a href="/#history">Development History</a>
        </nav>
        <div className="social"><a href={xUrl} target="_blank" rel="noreferrer">Official X</a><span>YouTube</span></div>
        <small>© 2026 MEMORIELA. All rights reserved.</small>
      </footer>
    </main>
  );
}

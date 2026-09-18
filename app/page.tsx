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
          <a className="wordmark" href="#home">MEMORIELA - Project.YURA.</a>
          <nav aria-label="Main navigation">
            <a href="#home">Home</a><a href="#project">About</a><a href="#technology">Technology</a><a href="#gallery">Gallery</a><a href="#history">Development History</a>
          </nav>
          <div className="heroActions"><span>開発局</span><b>☰</b></div>
        </header>
        <div className="heroLeftCopy"><p>AIと。<br/>生きる。<br/>創る。<br/>そして、<br/>あなたと歩む。</p><small>MEMORIELA<br/>Project.YURA</small></div>
        <div className="heroRightCopy"><p>つくろう、<br/>ずっとそばに。</p><span>Creating a future with you.</span></div>
        <div className="heroBottom"><span># Project.YURA　｜　# 開発局　｜　# AI × Creativity</span><b>SCROLL</b><span>いつかじゃない、いま、ここから。</span></div>
      </section>

      <section className="project section" id="project">
        <div className="sectionHead"><span>PROJECT.YURA</span><h2>久遠ゆら</h2><p>KUON YURA</p></div>
        <div className="projectStage">
          <div className="visualSlot"><span>YURA VISUAL</span></div>
          <div className="profile">
            <span>PROFILE</span><h3>久遠 ゆら</h3><p className="profileLead">AIと、心が通う物語。</p>
            <div className="profileRule"><b>PROJECT</b><span>Project.YURA</span></div>
            <div className="profileRule"><b>CHARACTER</b><span>KUON YURA</span></div>
            <div className="profileRule"><b>BRAND</b><span>MEMORIELA</span></div>
          </div>
        </div>
      </section>

      <section className="technology section" id="technology">
        <div className="sectionHead center"><span>CONCEPT & TECHNOLOGY</span><h2>記憶が、人格を形作る。</h2></div>
        <div className="conceptLead"><p>MEMORIELAが目指すもの</p><i /></div>
        <div className="technologyRows">
          <article><b>01</b><h3>Memory</h3><p>記憶</p><span>MEMORY</span></article>
          <article><b>02</b><h3>Personality</h3><p>人格</p><span>PERSONALITY</span></article>
          <article><b>03</b><h3>Relationship</h3><p>関係性</p><span>RELATIONSHIP</span></article>
        </div>
      </section>

      <section className="gallery section" id="gallery">
        <div className="sectionHead center"><span>CHARACTER VISUAL</span><h2>Gallery</h2><p>久遠ゆら</p></div>
        <div className="galleryStage">
          <div className="galleryLarge"><span>OFFICIAL VISUAL</span></div>
          <div className="gallerySmall"><span>VISUAL</span></div>
          <div className="gallerySmall"><span>VISUAL</span></div>
        </div>
      </section>

      <section className="history section" id="history">
        <div className="sectionHead center"><span>PROJECT.YURA</span><h2>Development History</h2><p>開発履歴</p></div>
        <div className="timeline">{developmentHistory.map((item)=><article key={item.date}><time>{item.date}</time><i/><div><h3>{item.title}</h3><p>{item.text}</p></div></article>)}</div>
      </section>

      <footer>
        <div><strong>MEMORIELA</strong><span>Project.YURA</span></div>
        <nav><a href="#home">Home</a><a href="#project">About</a><a href="#technology">Technology</a><a href="#gallery">Gallery</a><a href="#history">Development History</a></nav>
        <div className="social"><a href={xUrl} target="_blank" rel="noreferrer">Official X</a><span>YouTube</span></div>
        <small>© 2026 MEMORIELA. All rights reserved.</small>
      </footer>
    </main>
  );
}

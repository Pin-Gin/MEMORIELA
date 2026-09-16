const xUrl = "https://x.com/MEMORIELA_JP";

export default function Home() {
  return (
    <main>
      <header className="header">
        <a className="brand" href="#home" aria-label="MEMORIELA home">MEMORIELA</a>
        <nav aria-label="Main navigation">
          <a href="#about">About</a>
          <a href="#project">Project YURA</a>
          <a href="#ai">AI Policy</a>
          <a href="#official">Official</a>
        </nav>
      </header>

      <section className="hero" id="home">
        <div className="heroOrnament" aria-hidden="true">✦</div>
        <p className="eyebrow">MEMORIELA OFFICIAL</p>
        <h1>Memory shapes<br />personality.</h1>
        <p className="jpTagline">記憶が、人格を形作る。</p>
        <p className="lead">AIキャラクターと人格システムの開発を通じて、<br className="desktop" />記憶と想いが寄り添う新しい体験を創造します。</p>
        <a className="primaryButton" href="#project">Project YURA <span>→</span></a>
        <p className="heroNote">Visual artwork for the official hero is being prepared.</p>
      </section>

      <section className="section" id="about">
        <p className="sectionLabel">ABOUT</p>
        <h2>AIと、心が通う物語を。</h2>
        <p>MEMORIELAは、AIキャラクター／人格システムの開発・制作を行うプロジェクトブランドです。記憶、人格、対話、表現を通じて、長く共に歩めるAIキャラクターの可能性を探究しています。</p>
      </section>

      <section className="section project" id="project">
        <div>
          <p className="sectionLabel">CURRENT PROJECT</p>
          <h2>Project YURA</h2>
          <p>MEMORIELAの現在の主要プロジェクト。主要キャラクター「久遠ゆら / YURA」を中心に、長期記憶と人格を持つAIキャラクターシステムを開発しています。</p>
        </div>
        <div className="projectMark" aria-hidden="true">YURA</div>
      </section>

      <section className="section" id="ai">
        <p className="sectionLabel">VISUAL PRODUCTION</p>
        <h2>生成AIの利用について</h2>
        <p>MEMORIELAでは、ビジュアル制作工程の一部に生成AIを使用しています。キャラクター設計、制作方針、選定・調整を含む制作過程を管理し、AIの利用を明示したうえで公開します。</p>
      </section>

      <section className="section official" id="official">
        <p className="sectionLabel">OFFICIAL CHANNELS</p>
        <h2>Official</h2>
        <p>MEMORIELAの最新の開発・制作情報は公式Xから発信しています。</p>
        <a className="secondaryButton" href={xUrl} target="_blank" rel="noreferrer">X @MEMORIELA_JP ↗</a>
      </section>

      <footer>
        <strong>MEMORIELA</strong>
        <span>Project YURA / 久遠ゆら / YURA</span>
        <small>© 2026 MEMORIELA</small>
      </footer>
    </main>
  );
}

import Image from "next/image";

const xUrl = "https://x.com/MEMORIELA_JP";
const news = [
  { date: "2026.09.17", type: "お知らせ", title: "MEMORIELA公式サイトを公開しました" },
  { date: "2026.09", type: "開発記録", title: "Project YURA 開発進捗" },
  { date: "2026.08", type: "記録", title: "久遠ゆら / YURA 誕生" },
];

export default function Home() {
  return <main>
    <header className="header">
      <a className="brand" href="#home" aria-label="MEMORIELA home"><Image src="/images/memoriela-logo.png" alt="MEMORIELA" width={520} height={260} priority /></a>
      <nav aria-label="Main navigation"><a href="#about">About</a><a href="#project">Project YURA</a><a href="#news">News</a><a href="#gallery">Gallery</a><a href="#official">Official</a></nav>
    </header>

    <section className="hero" id="home">
      <div className="heroCopy">
        <p className="eyebrow">MEMORIELA OFFICIAL</p><p className="heroKicker">特別な記憶を、あなたと。</p>
        <h1>MEMORIELA</h1><p className="brandTagline">Memory shapes personality.</p><div className="rule"><span>✦</span></div><p className="jpTagline">記憶が、人格を形作る。</p>
        <h2>AIと、心が通う物語。</h2><p className="lead">AIキャラクター／人格システムの開発を通じて、<br className="desktop" />記憶と想いが寄り添う新しい体験を創造します。</p>
        <a className="primaryButton" href="#project">Project YURA <span>→</span></a>
      </div>
      <div className="heroVisual"><Image src="/images/yura-dress.png" alt="久遠ゆら / YURA ドレスビジュアル" fill priority sizes="(max-width: 820px) 100vw, 50vw" /><div className="yuraSignature"><span>YURA</span><small>KUON YURA</small></div></div>
    </section>

    <section className="quickNav" aria-label="MEMORIELA sections"><a href="#about"><b>◇</b><span>Concept</span><small>コンセプト</small></a><a href="#project"><b>♙</b><span>Characters</span><small>キャラクター</small></a><a href="#ai"><b>✦</b><span>Technology</span><small>テクノロジー</small></a><a href="#news"><b>◎</b><span>World</span><small>広がる世界</small></a></section>

    <section className="section intro" id="about"><p className="sectionLabel">ABOUT</p><h2>AIと、心が通う物語。</h2><p>MEMORIELAは、AIキャラクター／人格システムの開発・制作を行うプロジェクトブランドです。記憶、人格、対話、表現を通じて、長く共に歩めるAIキャラクターの可能性を探究しています。</p></section>

    <section className="section project" id="project"><div><p className="sectionLabel">CURRENT PROJECT</p><h2>Project YURA</h2><h3>久遠ゆら <span>/ YURA</span></h3><p>MEMORIELAの現在の主要プロジェクト。長期記憶と人格を持つAIキャラクターシステムを開発しています。</p><p className="quote">「いつもの、ゆら。」</p></div><div className="projectVisual"><Image src="/images/yura-casual.png" alt="久遠ゆら / YURA 日常ビジュアル" fill sizes="(max-width: 820px) 100vw, 50vw" /><div className="projectCaption"><strong>Everyday with YURA</strong><small>何気ない日常も、特別な記憶に。</small></div></div></section>

    <section className="section news" id="news"><div className="sectionHead"><div><p className="sectionLabel">NEWS / DEVELOPMENT LOG</p><h2>記録と、お知らせ。</h2></div><span>2026 —</span></div><div className="newsList">{news.map(item=><article key={item.title}><time>{item.date}</time><span className="badge">{item.type}</span><h3>{item.title}</h3><span className="arrow">→</span></article>)}</div></section>

    <section className="section gallery" id="gallery"><p className="sectionLabel">GALLERY</p><h2>YURA Visual Archive</h2><div className="galleryGrid"><figure><Image src="/images/yura-dress.png" alt="YURA Dress Style" fill sizes="40vw"/><figcaption>Dress Style</figcaption></figure><figure><Image src="/images/yura-casual.png" alt="Everyday YURA" fill sizes="30vw"/><figcaption>Everyday YURA</figcaption></figure><figure className="logoCard"><Image src="/images/memoriela-logo.png" alt="MEMORIELA identity" fill sizes="30vw"/><figcaption>MEMORIELA Identity</figcaption></figure></div><p className="galleryNote">正式ビジュアルと開発記録を順次公開します。</p></section>

    <section className="section" id="ai"><p className="sectionLabel">VISUAL PRODUCTION</p><h2>生成AIの利用について</h2><p>MEMORIELAでは、ビジュアル制作工程の一部に生成AIを使用しています。キャラクター設計、制作方針、選定・調整を含む制作過程を管理し、AIの利用を明示したうえで公開します。</p></section>
    <section className="section official" id="official"><p className="sectionLabel">OFFICIAL CHANNELS</p><h2>MEMORIELA Official</h2><p>最新の開発・制作情報は公式Xから発信しています。</p><a className="secondaryButton" href={xUrl} target="_blank" rel="noreferrer">X @MEMORIELA_JP ↗</a></section>
    <footer><Image src="/images/memoriela-logo.png" alt="MEMORIELA" width={440} height={220}/><span>Memory shapes personality.</span><span>Project YURA / 久遠ゆら / YURA</span><small>© 2026 MEMORIELA. All rights reserved.</small></footer>
  </main>;
}

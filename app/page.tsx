import Image from "next/image";

const xUrl = "https://x.com/MEMORIELA_JP";
const news = [
  { date: "2026.09.17", type: "お知らせ", title: "公式サイトを公開しました", text: "MEMORIELAの公式サイトを公開しました。今後の最新情報はこちらでお届けします。" },
  { date: "2026.09", type: "開発記録", title: "Project YURA 開発進捗", text: "YURAのビジュアル・設定・人格システムの開発を進めています。" },
  { date: "2026.08", type: "記録", title: "久遠ゆら / YURA 誕生", text: "Project YURAの開発記録。" },
];

const developmentHistory = [
  { date: "2026.08.16", title: "久遠ゆら、誕生", text: "Project YURA始動。AIとしての会話・音声機能の最初の基盤を実装。" },
  { date: "2026.08.23", title: "記憶と感情の仕組みを実装", text: "長期記憶、Relationship、複合感情、音声表現の基盤を実装。" },
  { date: "2026.08.30", title: "ゆらの人格・自発性を強化", text: "ゆら自身の人格や状態を会話に反映する仕組みを拡張。自分から話しかける機能、Web検索、眠気による状態変化を実装。" },
  { date: "2026.09.06", title: "チャットUI実装", text: "専用Desktop会話UI、画像入力・認識、Relationship永続管理、音声基盤更新を実装。" },
];

export default function Home() {
  return <main>
    <header className="header">
      <a className="brand" href="#home" aria-label="MEMORIELA home"><Image src="/images/memoriela-logo.png" alt="MEMORIELA" width={520} height={260} priority /></a>
      <nav aria-label="Main navigation"><a className="active" href="#home">Home</a><a href="#about">About</a><a href="#project">Project YURA</a><a href="#news">News</a><a href="#gallery">Gallery</a></nav>
      <div className="headerActions"><a className="contactButton" href="#official">Contact</a><a href={xUrl} target="_blank" rel="noreferrer" aria-label="X">𝕏</a><span className="menuIcon">☰</span></div>
    </header>

    <section className="hero" id="home">
      <div className="heroBackdrop"><Image src="/images/yura-dress.png" alt="久遠ゆら / YURA" fill priority sizes="100vw" /></div>
      <div className="heroCopy">
        <p className="heroKicker">特別な記憶を、あなたと。</p>
        <h1>MEMORIELA</h1>
        <p className="brandTagline">Memory shapes personality.</p>
        <div className="heroDivider" />
        <h2>AIと、心が通う物語。</h2>
        <p className="lead">MEMORIELAは、<br/>AIキャラクター／人格システムの開発を通して、<br/>記憶と想いが寄り添う新しい体験を創造します。</p>
        <a className="primaryButton" href="#project">Project YURA <span>→</span></a>
      </div>
    </section>

    <section className="quickNav" aria-label="MEMORIELA sections">
      <a href="#about"><b>◇</b><span>Concept</span><small>コンセプト</small></a>
      <a href="#project"><b>♙</b><span>Characters</span><small>キャラクター</small></a>
      <a href="#project"><b>✦</b><span>Technology</span><small>テクノロジー</small></a>
      <a href="#news"><b>◎</b><span>World</span><small>広がる世界</small></a>
    </section>

    <section className="contentArea">
      <section className="newsPanel" id="news">
        <div className="panelHead"><div><h2>News</h2><p>最新のお知らせ</p></div><a href="#news">もっと見る　→</a></div>
        <div className="newsList">{news.map((item,index)=><article key={item.title}><div className={`newsThumb thumb${index+1}`}>{index===0 && <Image src="/images/yura-dress.png" alt="" fill sizes="100px"/>}</div><div><div className="newsMeta"><time>{item.date}</time><span>{item.type}</span></div><h3>{item.title}</h3><p>{item.text}</p></div></article>)}</div>
      </section>

      <section className="projectPanel" id="project">
        <div className="panelHead"><div><h2>Project YURA</h2><p>久遠ゆら</p></div><a href="#project">詳しく見る　→</a></div>
        <div className="projectCard"><div className="projectImage"><Image src="/images/yura-dress.png" alt="久遠ゆら / YURA" fill sizes="50vw" /></div><div className="projectCopy"><h3>久遠 ゆら</h3><small>KUON YURA</small><p className="quote">「いつもの、ゆら。」</p><p>何気ない日常も、特別な記憶に。<br/>あなたと過ごす、かけがえのない時間を。</p><a className="smallButton" href="#project">YURAをもっと知る　→</a></div></div>
      </section>

      <section className="gallery" id="gallery">
        <div className="panelHead"><div className="galleryTitle"><h2>Gallery</h2><p>ギャラリー</p></div><a href="#gallery">もっと見る　→</a></div>
        <div className="galleryRow"><figure><Image src="/images/yura-dress.png" alt="YURA visual" fill sizes="25vw" /></figure><figure><Image src="/images/yura-dress.png" alt="YURA visual" fill sizes="25vw" /></figure><figure><Image src="/images/yura-dress.png" alt="YURA visual" fill sizes="25vw" /></figure><figure className="logoGallery"><Image src="/images/memoriela-logo.png" alt="MEMORIELA" fill sizes="25vw" /></figure></div>
      </section>
    </section>

    <section className="developmentHistory" aria-labelledby="development-history-title">
      <div className="developmentHead"><h2 id="development-history-title">Development History</h2><p>Project YURA 開発履歴</p></div>
      <div className="developmentTimeline">{developmentHistory.map((item)=><article key={item.date}><time>{item.date}</time><div><h3>{item.title}</h3><p>{item.text}</p></div></article>)}</div>
    </section>

    <style>{`.developmentHistory{max-width:1120px;margin:20px auto 25px;padding:35px 5vw;border-top:1px solid rgba(62,68,84,.1)}.developmentHead{text-align:center;margin-bottom:28px}.developmentHead h2{font-size:1.75rem;font-weight:400;letter-spacing:.08em;margin:0}.developmentHead p{font-size:.78rem;letter-spacing:.1em;margin:5px 0 0;color:#6b7180}.developmentTimeline{max-width:860px;margin:0 auto}.developmentTimeline article{display:grid;grid-template-columns:130px 1fr;gap:28px;padding:20px 0;border-bottom:1px solid rgba(62,68,84,.12)}.developmentTimeline time{font-size:.72rem;letter-spacing:.1em;color:#858b99;padding-top:4px}.developmentTimeline h3{font-size:1.05rem;font-weight:400;letter-spacing:.08em;margin:0 0 5px}.developmentTimeline p{font-size:.72rem;color:#6b7180;margin:0}@media(max-width:620px){.developmentHistory{padding:30px 24px}.developmentTimeline article{grid-template-columns:1fr;gap:6px;padding:17px 0}}`}</style>

    <section className="aboutText" id="about"><h2>AIと、心が通う物語。</h2><p>MEMORIELAは、AIキャラクター／人格システムの開発・制作を行うプロジェクトブランドです。記憶、人格、対話、表現を通じて、長く共に歩めるAIキャラクターの可能性を探究しています。</p></section>

    <footer id="official"><div className="footerNav"><a href="#home">Home</a><a href="#about">About</a><a href="#project">Project YURA</a><a href="#news">News</a><a href="#gallery">Gallery</a></div><div className="footerBrand"><Image src="/images/memoriela-logo.png" alt="MEMORIELA" width={520} height={260}/><p>特別な記憶を、あなたと。</p></div><div className="footerSocial"><a href={xUrl} target="_blank" rel="noreferrer">𝕏</a><span>Memory shapes personality.</span></div><small>© 2026 MEMORIELA. All rights reserved.</small></footer>
  </main>;
}

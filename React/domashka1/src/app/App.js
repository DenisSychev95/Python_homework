
import './App.css';
import Header from '../header/Header';
import Content from '../content/Content';
import Footer from '../footer/Footer';

function App(props) {
  console.log(props);
  let { group, album, released, studio, songs} = props
  console.log(group);


  return (
    <div className="App">
      <Header group={group} album={album} released={released} />
      <Content songs={songs}/>
      <Footer released={released} studio={studio} />

    </div>
  );
}

export default App;

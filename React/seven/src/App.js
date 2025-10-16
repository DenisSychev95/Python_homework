import Users from './components/users/Users';
import { useState, useEffect } from 'react';
import Succses from './components/succses/Success';
import './App.css';

function App() {

  const [users, setUsers] = useState([]);

  useEffect(() => {
    fetch('https://reqres.in/api/users', {
      headers: {
        'x-api-key': 'reqres-free-v1'
      }
    })
      .then(res => res.json())
      .then(json => setUsers(json.data))
  }, []);

  const [searchValue, setSearchValue] = useState("");

  const onChangeValue = (event) => {
    setSearchValue(event.target.value)
  }

  const [invites, setInvites] = useState([]);

  const onClickInvite = (id) => {
    if (invites.includes(id)) {
      setInvites(prev => prev.filter(ch => ch !== id));
    }
    else {
      setInvites(prev => [...prev, id])
    }
  }

  const [succses, setSuccses] = useState(false);

  const onClickSetInvites=()=>{
    setSuccses(true)
  }

  return (
    <div className="main">
      {
        succses? <Succses count={invites.length}/>: 
      <Users
        items={users}
        onChangeValue={onChangeValue}
        searchValue={searchValue}
        invites={invites}
        onClickInvite={onClickInvite}
        onClickSetInvites={onClickSetInvites} />
       } 
    </div>
  );
}

export default App;

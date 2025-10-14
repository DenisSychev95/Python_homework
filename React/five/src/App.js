import './App.css';
import Counter from './Counter';
/* import Person from './Person';  */
/* import Modal from './Modal'; */
/* import Item from './Item'; */
import { useState} from 'react';
import Text from './Text';
/* import Task from './Task';
import Form from './Form'; */

function App() {

  /*   let [tasks, setTasks] = useState([
      { text: "Выучить JavaSpript", done: false },
      { text: "Познакомиться с  React", done: false },
      { text: "Устроиться на работу ", done: false }
    ])
  
    let addTask = (text) => {
      let newTask = [...tasks, { text }];
      setTasks(newTask)
    }
  
    let doneTask = (index) => {
      let newTask = [...tasks];
      newTask[index].done = !newTask[index].done;
      setTasks(newTask)
    }
  
    let deleteTask = (index) => {
      let newTask = [...tasks];
      newTask.splice(index, 1);
      setTasks(newTask);
    } */

  let [isCounter, setCounter] = useState(true);



  return (


    <div className="App">
      {/*       {console.log(tasks)
      } */}
      <div className="task-list">

        <button onClick={() => setCounter(!isCounter)}>Toggle Counter</button>
        {isCounter && <Counter />}

        <Text/>



        {/*<Person/> */}
        {/* <Modal /> */}
        {/* <Item /> */}

        {/*  {
          tasks.map((task, index) =>
            <Task doneTask={doneTask}
              deleteTask={deleteTask}
              index={index}
              key={index}
              task={task} />)
        }
        <Form addTask={addTask} /> */}
      </div>

    </div>
  );
}

export default App;

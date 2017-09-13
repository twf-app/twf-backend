const express = require('express')
const multer = require('multer')
const utilities = require('./utilities.js')

let app = express()

let db = [{
    uid: 0,
    todos: [{
        tid: 0,
        desc: '',
        todoURL: '0/todo/0'
      }]
    }]

app.get(':uid/todo/:tid', function(req,res){
    const uid = req.params.uid
    const tid = req.params.tid

    if(!isNaN(uid) && db[uid] && !isNaN(tid) && db[uid].todos[tid]){
        res.status(200).send(JSON.stringify(db[uid]))
    } else {
        res.status(406).send("not a number or not yet created")
    }
})

// what will we be sending? just text? how to do best?
app.put(':uid/todo/:tid', function(req,res){
    const uid = req.params.uid
    const tid = req.params.tid


    if(!isNaN(uid) && !isNaN(tid)){
        let desc = req.desc
        let newObj = db[uid].todos[tid]
        newObj.desc = desc
        db[uid].todos[tid] = newObj
        res.sendStatus(200)
    } else {
        res.status(406).send("not a number or no file attached")
    }
})

app.post('/newuser', function(req,res){
    const uid = utilities.getCurrentId(db)
    const user = {
        uid
    }

    db.push(user);
    res.status(201).send(JSON.stringify(user))
})

app.post('/newtodo/:uid', function(req,res){
    const uid = req.params.uid
    const tid = utilities.getCurrentId(db[uid].todos)

    const todo = {
        tid,
        desc: '',
        todoURL: `${uid}/todos/${tid}`
    }

    db[uid].todos.push(todo);
    res.status(201).send(JSON.stringify(user))
})

const server = app.listen(3000, function(){
    console.log("server running...")
})

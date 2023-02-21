import express from 'express'
import cors from 'cors'
import 'express-async-errors'
import unknownEndPointHandler from './middleware/unknownEndpoint'
import errorHandler from './middleware/errorHandler'
import helloRoutes from './routes/hello'

const app = express()

app.use(cors())
app.use(express.json())

app.use('/', helloRoutes)

app.use(unknownEndPointHandler)
app.use(errorHandler)

export default app

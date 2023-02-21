import express from 'express'
import { getHello } from '../controllers/hello'

const router = express.Router()

// Project routes
router.get('/', getHello)

export default router

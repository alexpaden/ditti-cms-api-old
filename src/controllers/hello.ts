import { Request, Response } from 'express'

export const getHello = async (_req: Request, res: Response) => {
  const hello_string = 'Hello World!'

  res.json(hello_string)
}

import fs from 'fs'
import path from 'path'

function getAllFiles(directoryPath: string): string[] {
  const files: string[] = []
  fs.readdirSync(directoryPath).forEach((file: string) => {
    const filePath = path.join(directoryPath, file)
    if (fs.statSync(filePath).isDirectory()) {
      files.push(...getAllFiles(filePath))
    } else if (
      filePath.endsWith('.ts') &&
      !filePath.endsWith(path.basename(process.argv[1]))
    ) {
      files.push(filePath)
    }
  })
  return files
}

const folderPath = '.'
const allFiles = getAllFiles(folderPath)

let outputString = ''
allFiles.forEach((filePath: string) => {
  const contents = fs.readFileSync(filePath, { encoding: 'utf8' })
  outputString += `\n\n\n\n/* ${filePath} */\n${contents}\n/*\n`
})

fs.writeFileSync('full_code.txt', outputString)

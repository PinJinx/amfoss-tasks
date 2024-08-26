import System.Directory (getCurrentDirectory)
import System.FilePath ((</>))
import System.IO (readFile, writeFile)

main :: IO ()
main = do
    scriptDir <- getCurrentDirectory
    let inputFilePath = scriptDir </> "input.txt"
    let outputFilePath = scriptDir </> "output.txt"
    content <- readFile inputFilePath
    writeFile outputFilePath content
    putStrLn "File copied"

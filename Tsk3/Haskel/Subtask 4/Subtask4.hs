import System.IO
import System.Directory
import System.FilePath

main :: IO ()
main = do
    -- Get the current dir
    scriptDir <- getCurrentDirectory
    
    -- Openfile
    let inputPath = scriptDir </> "input.txt"
    inputHandle <- openFile inputPath ReadMode
    inputContent <- hGetContents inputHandle
    let n = read inputContent :: Int
    let adjustedN = if n `mod` 2 == 0 then n - 1 else n

    -- Ope n output file
    let outputPath = scriptDir </> "output.txt"
    outputHandle <- openFile outputPath WriteMode

    -- Write the top half of the diamond
    writeTopHalf outputHandle adjustedN
    writeBottomHalf outputHandle adjustedN
    hClose inputHandle
    hClose outputHandle

writeTopHalf :: Handle -> Int -> IO ()
writeTopHalf handle n = loop n 1
  where
    loop _ i | i > n = return ()
    loop n' i = do
        let spaces = replicate ((n' - i) `div` 2) ' '
        let stars = replicate i '*'
        hPutStrLn handle (spaces ++ stars)
        loop n' (i + 2)

writeBottomHalf :: Handle -> Int -> IO ()
writeBottomHalf handle n = loop n (n - 2)
  where
    loop _ i | i <= 0 = return ()
    loop n' i = do
        let spaces = replicate ((n' - i) `div` 2) ' '
        let stars = replicate i '*'
        hPutStrLn handle (spaces ++ stars)
        loop n' (i - 2)

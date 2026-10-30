# 🇧🇩 Bangladesh ASCII Map in C

A lightweight, high-density terminal ASCII art generator rendering the geographic map of Bangladesh using run-length string decompression.

---

## 🗺️ Preview

```text
     *                                                          
    ****                                                        
       ***  ***                                                 
     **********                                                 
   **************     **                                        
  ***********************                                       
  **********************                                        
     ********************                                       
       ******************                                       
            *************                                       
              **************                      *****         
       ****************************************************     
      ******************************************************    
   * ****************************************************       
  *******************************************************       
******************************************************* *       
   **************************************************           
      ***********************************************           
           **************************************               
          ***********************************                   
           *********************************                    
        ***********************************          ****       
         **********************************          ****       
           *********************************      ********      
          ***********************************      *******      
              ******************************* *    ********     
             *********************************** **********     
             ***********************************************    
             ********************************* **************   
             *******************************    *************   
              **************************   *      ***********   
              *************************            ***  ******  
               ************************            *    ******  
               ************************                 ******  
               **  **************                      *******  
               **  **** **   ***                       *******  
                *                                       ******  
                                                         ****** 
                                                       **     * 
```

---

## 🧠 How the Algorithm Works

The compressed map is stored inside a compact 137-character ASCII string `magic`.
- **Run-Length Storage**: Each byte `c` in the string encodes the run length of a character:
  $$\text{length} = 126 - c$$
- **Alternating Symbols**:
  - Even index (`i % 2 == 0`): Run of spaces (`' '`).
  - Odd index (`i % 2 == 1`): Run of asterisks (`'*'`).
- **Terminal Grid**: The decompressed stream automatically wraps every 64 characters to form a 64-column geographic map grid.

---

## 🔧 Build & Run

### C Implementation (`Ccode.c`)

#### On Linux / macOS:
```bash
gcc -Wall -Wextra -pedantic -std=c99 Ccode.c -o bd_map
./bd_map
```

#### On Windows (MinGW / PowerShell):
```powershell
gcc -Wall -Wextra -pedantic -std=c99 Ccode.c -o bd_map.exe
.\bd_map.exe
```

---

### Python Encoder & Decoder (`ascii_map_generator.py`)

Run the included Python encoder/decoder tool:
```bash
python ascii_map_generator.py
```
This script validates the round-trip conversion between the raw ASCII text and the compressed C string representation.

---

## 📄 License
Open source under the [MIT License](LICENSE).

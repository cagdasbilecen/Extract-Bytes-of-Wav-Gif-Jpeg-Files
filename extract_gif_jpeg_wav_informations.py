
#   Cagdas Bilecen # 2014510015

# FILE PATHS ...
# use "r" before the path as follows or code will not work...
pathOfWav = r"C:\Users\cadob\OneDrive\Masaüstü\sample.wav" 
pathOfGif = r"C:\Users\cadob\OneDrive\Masaüstü\sample.gif"
pathOfJpeg = r"C:\Users\cadob\OneDrive\Masaüstü\sample.jpg"



############ READ WAV FILE ############


def readWavFile(strWAVFile):
    
    import os
    import struct
    import logging

    logging.basicConfig(level=logging.DEBUG)
    def DumpHeaderOutput(structHeaderFields):
        print ("##### Results of Wav File: #####")
        for key in structHeaderFields.keys():
            print ("%s: " % (key), structHeaderFields[key])
        print ("\n")

        # end for
    # Open file
    try:
        fileIn = open(strWAVFile, 'rb')
    except (IOError):
        logging.debug("Could not open input file %s" % (strWAVFile))
        return
    # end try
    # Read in  data
    bufHeader = fileIn.read(38)
    
    # endif
    stHeaderFields = {'ChunkSize' : 0, 'Format' : '',
        'Subchunk1Size' : 0, 'AudioFormat' : 0,
        'NumChannels' : 0, 'SampleRate' : 0,
        'ByteRate' : 0, 'BlockAlign' : 0,
        'BitsPerSample' : 0, 'Filename': ''}
    # Parse fields
    stHeaderFields['ChunkSize'] = struct.unpack('<L', bufHeader[4:8])[0]
    stHeaderFields['Format'] = bufHeader[8:12]
    stHeaderFields['Subchunk1Size'] = struct.unpack('<L', bufHeader[16:20])[0]
    stHeaderFields['AudioFormat'] = struct.unpack('<H', bufHeader[20:22])[0]
    stHeaderFields['NumChannels'] = struct.unpack('<H', bufHeader[22:24])[0]
    stHeaderFields['SampleRate'] = struct.unpack('<L', bufHeader[24:28])[0]
    stHeaderFields['ByteRate'] = struct.unpack('<L', bufHeader[28:32])[0]
    stHeaderFields['BlockAlign'] = struct.unpack('<H', bufHeader[32:34])[0]
    stHeaderFields['BitsPerSample'] = struct.unpack('<H', bufHeader[34:36])[0]
    
    # Print output
    stHeaderFields['Filename'] = os.path.basename(strWAVFile)
    DumpHeaderOutput(stHeaderFields)
    # Close file
    fileIn.close()
    

 

   
readWavFile(pathOfWav) 

############# READ GIF FILE #################

def readGifFile(strGifFile):
    
    import os
    import struct
    import logging
    logging.basicConfig(level=logging.DEBUG)
    def DumpHeaderOutput(structHeaderFields):
        print ("##### Results of Gif File: #####")

        for key in structHeaderFields.keys():
            print ("%s: " % (key), structHeaderFields[key])
        print ("\n")
        # end for
    # Open file
    try:
        fileIn = open(strGifFile, 'rb')
    except (IOError):
        logging.debug("Could not open input file %s" % (strGifFile))
        return
    # end try
    # Read in 38 byte of data.. its enough for the header informations of gif file.
    bufHeader = fileIn.read(38)
    
    # endif
    stHeaderFields = {'ImageWidth' : 0, 'ImageHeight' : 0, 'BackgroundColor' : '',
        'NumberOfImagesInGifAnimation' : 0}
    # Parse fields
    stHeaderFields['ImageWidth'] = struct.unpack('<H', bufHeader[6:8])[0]
    stHeaderFields['ImageHeight'] = struct.unpack('<H',bufHeader[8:10])[0]
    stHeaderFields['BackgroundColor'] = bufHeader[11:12]
    stHeaderFields['NumberOfImagesInGifAnimation'] = struct.unpack('<L', bufHeader[16:20])[0]
    
   
    # Print output
    stHeaderFields['Filename'] = os.path.basename(strGifFile)
    DumpHeaderOutput(stHeaderFields)
    # Close file
    fileIn.close()

readGifFile(pathOfGif) 


### to calculate filesize from jpeg##
def jpegSize(file):
    with open(file, 'rb') as f:
        s = f.read()
    return s.find(b'\xff\xd9')+2

def isEdited(file):
    with open(file, 'rb') as f:
        s = f.read()
    
    if b'\xff\xed' in s:        
        return "edited"
    else :
        return "not edited"
  
    
         
#################### READ JPEG FILE ################ 
def readJpegFile(strJpegFile):
    import os
    import struct
    import logging
    logging.basicConfig(level=logging.DEBUG)
    
    def DumpHeaderOutput(structHeaderFields):
        print ("##### Results of Jpeg File: #####")

        for key in structHeaderFields.keys():
            print ("%s: " % (key), structHeaderFields[key])

        # end for
    # Open file
    try:
        fileIn = open(strJpegFile, 'rb')
    except (IOError):
        logging.debug("Could not open input file %s" % (strJpegFile))
        return
    # end try
    bufHeader = fileIn.read(1343)
   
    
    stHeaderFields = {'Big/LittleEndian' : 0, 'FileSize' : 0, 'isEdited' : 0}
    # Parse fields
    if(struct.unpack('<H',bufHeader[0:2])[0]==55551) :
        stHeaderFields['Big/LittleEndian'] = "Little Endian"
    else:
        stHeaderFields['Big/LittleEndian'] = "Big Endian"


           
    
    #horizontal_resolution = struct.unpack('<H',bufHeader[160:162])[0]
    #vertical_resolution = struct.unpack('<H',bufHeader[160:162])[0]
    stHeaderFields['FileSize'] = jpegSize(pathOfJpeg)
    stHeaderFields['isEdited'] = isEdited(pathOfJpeg)
    
   
    # Print output
    stHeaderFields['Filename'] = os.path.basename(strJpegFile)
    DumpHeaderOutput(stHeaderFields)
    # Close file
    fileIn.close()

readJpegFile(pathOfJpeg) 



#jpegSize(pathOfJpeg)
    



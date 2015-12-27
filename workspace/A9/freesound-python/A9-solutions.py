import soundDownload as SD
import soundAnalysis as SA

my_API_Key = "863123c217dfe28ce4a9ebe0dd7efacdc8adfa35"
my_topNResults = 20

# Get sound info set-1
print "Starting downloading set-1:"
print "-----------"
SD.downloadSoundsFreesound(queryText = "cello", API_Key = my_API_Key, outputDir = "./testDownload", topNResults = my_topNResults, duration = (0,10), tag = "cello")
print "-----------"
print "Download of set-1 completed"
print "\n"

# Get sound info set-2
print "Starting downloading set-2:"
print "-----------"
SD.downloadSoundsFreesound(queryText = "guitar", API_Key = my_API_Key, outputDir = "./testDownload", topNResults = my_topNResults, duration = (0,10), tag = "guitar")
print "-----------"
print "Download of set-2 completed"
print "\n"

# Get sound info set-3
print "Starting downloading set-3:"
print "-----------"
SD.downloadSoundsFreesound(queryText = "clarinet", API_Key = my_API_Key, outputDir = "./testDownload", topNResults = my_topNResults, duration = (0,10), tag = "single-note")
print "-----------"
print "Download of set-3 completed"
print "\n"

# Get sound info set-4 for kNN exercise
print "Starting downloading set-4:"
print "-----------"
SD.downloadSoundsFreesound(queryText = "trumpet", API_Key = my_API_Key, outputDir = "./testCluster", topNResults = 2, duration = (0,10), tag = "single-note")
print "-----------"
print "Download of set-4 completed"
print "\n"

#Get sound visual info
SA.showDescriptorMapping()

print "Starting plotting:"
#idx = 1
#while(idx<=16):
#    SA.descriptorPairScatterPlot("./testDownload", descInput = (0,idx))
#    print "idx = " + str(idx)
#    print "\n"
#    idx = idx + 1

SA.descriptorPairScatterPlot("./testDownload", descInput = (0,15))
print "Plot completed"
print "\n"

print "Starting clustering:"
SA.clusterSounds("./testDownload", nCluster = 3, descInput = [0,1,14,15])
print "Clustering completed"
print "\n"

print "Starting kNN clustering:"
SA.classifySoundkNN("./testCluster/trumpet/247171/247171_637616-lq.json","./testDownload/", 3, descInput = [0,1,14,15])
print "kNN clustering completed"
print "\n"

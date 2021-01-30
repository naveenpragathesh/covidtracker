# VDR_REN_STAR_READING
temp = """
"SchoolYear" VARCHAR(16777216),
	"StudentSourcedID" VARCHAR(16777216),
	"StudentStateID" FLOAT,
	"StudentEmail" VARCHAR(16777216),
	"StudentFirstName" VARCHAR(16777216),
	"StudentMiddleName" VARCHAR(16777216),
	"StudentLastName" VARCHAR(16777216),
	"CurrentGrade" NUMBER(38,0),
	"EnrollmentStatus" VARCHAR(16777216),
	"DistrictRenaissanceID" VARCHAR(16777216),
	"SchoolIdentifier" FLOAT,
	"SchoolStateID" FLOAT,
	"SchoolName" VARCHAR(16777216),
	"CourseCode" VARCHAR(16777216),
	"CourseName" VARCHAR(16777216),
	"TeacherIdentifier" VARCHAR(16777216),
	"TeacherStateID" FLOAT,
	"AssessmentID" VARCHAR(16777216),
	"LaunchDate" VARCHAR(16777216),
	"CompletedDate" VARCHAR(16777216),
	"CompletedDateLocal" VARCHAR(16777216),
	"AssessmentNumber" NUMBER(38,0),
	"AssessmentType" VARCHAR(16777216),
	"AssessmentStatus" VARCHAR(16777216),
	"DeactivationReason" FLOAT,
	"GradePlacement" FLOAT,
	"Grade" VARCHAR(16777216),
	"ExtraTime" VARCHAR(16777216),
	"ScaledScore" NUMBER(38,0),
	"StandardErrorOfMeasurement" FLOAT,
	"RaschScore" FLOAT,
	"UnifiedScore" NUMBER(38,0),
	"PartnershipForAssessmentOfReadinessForCollegeAndCareers" FLOAT,
	"SmarterBalancedAssessmentConsortium" FLOAT,
	"OpenGrowthScore" FLOAT,
	"GradeEquivalent" VARCHAR(16777216),
	"PercentileRank" NUMBER(38,0),
	"NormalCurveEquivalent" FLOAT,
	"InstructionalReadingLevel" VARCHAR(16777216),
	"EstimatedOralReadingFluency" FLOAT,
	"LowerZoneOfProximalDevelopment" FLOAT,
	"UpperZoneOfProximalDevelopment" FLOAT,
	"Lexile" VARCHAR(16777216),
	"LowerLexileZoneOfProximalDevelopment" FLOAT,
	"UpperLexileZoneOfProximalDevelopment" FLOAT,
	"TotalTimeInSeconds" NUMBER(38,0),
	"TotalCorrect" FLOAT,
	"TotalPossible" FLOAT,
	"Grade3_AssessmentAttempts" NUMBER(38,0),
	"Grade3_PassingStatus" FLOAT,
	"Grade3_PassingScore" FLOAT,
	"StudentGrowthPercentileFallFall" FLOAT,
	"StudentGrowthPercentileFallSpring" FLOAT,
	"StudentGrowthPercentileFallWinter" FLOAT,
	"StudentGrowthPercentileSpringFall" FLOAT,
	"StudentGrowthPercentileSpringSpring" FLOAT,
	"StudentGrowthPercentileWinterSpring" FLOAT,
	"ScreeningPeriodWindowName" VARCHAR(16777216),
	"ScreeningWindowStartDate" VARCHAR(16777216),
	"ScreeningWindowEndDate" VARCHAR(16777216),
	"RenaissanceBenchmarkCategoryName" VARCHAR(16777216),
	"RenaissanceBenchmarkCategoryLevel" FLOAT,
	"RenaissanceBenchmarkCategoryNumberOfLevels" NUMBER(38,0),
	"RenaissanceBenchmarkCategoryMinPercentileRank" FLOAT,
	"RenaissanceBenchmarkCategoryMaxPercentileRank" FLOAT,
	"StateBenchmarkAssessmentName" VARCHAR(16777216),
	"StateBenchmarkCategoryName" VARCHAR(16777216),
	"StateBenchmarkProficient" VARCHAR(16777216),
	"StateBenchmarkCategoryLevel" FLOAT,
	"StateBenchmarkNumberOfCategoryLevels" FLOAT,
	"StateBenchmarkMinScaledScore" FLOAT,
	"StateBenchmarkMaxScaledScore" FLOAT,
	"DistrictBenchmarkCategoryName" VARCHAR(16777216),
	"DistrictBenchmarkProficient" VARCHAR(16777216),
	"DistrictBenchmarkCategoryLevel" FLOAT,
	"DistrictBenchmarkNumberOfCategoryLevels" FLOAT,
	"DistrictBenchmarkMinPercentileRank" FLOAT,
	"DistrictBenchmarkMaxPercentileRank" FLOAT,
	"SchoolBenchmarkCategoryName" VARCHAR(16777216),
	"SchoolBenchmarkProficient" VARCHAR(16777216),
	"SchoolBenchmarkCategoryLevel" FLOAT,
	"SchoolBenchmarkNumberOfCategoryLevels" FLOAT,
	"SchoolBenchmarkMinPercentileRank" FLOAT,
	"SchoolBenchmarkMaxPercentileRank" FLOAT,
	"CurrentSGP" FLOAT,
	"TakenAt" VARCHAR(16777216)
)
"""
# VDR_REN_ACCELERATED_READER
temp1 = """
	"SchoolYear" VARCHAR(16777216),
	"StudentSourcedID" VARCHAR(16777216),
	"StudentStateID" FLOAT,
	"StudentEmail" VARCHAR(16777216),
	"StudentFirstName" VARCHAR(16777216),
	"StudentMiddleName" VARCHAR(16777216),
	"StudentLastName" VARCHAR(16777216),
	"CurrentGrade" VARCHAR(16777216),
	"EnrollmentStatus" VARCHAR(16777216),
	"DistrictRenaissanceID" VARCHAR(16777216),
	"SchoolIdentifier" FLOAT,
	"SchoolStateID" FLOAT,
	"SchoolName" VARCHAR(16777216),
	"CourseCode" VARCHAR(16777216),
	"CourseName" VARCHAR(16777216),
	"TeacherIdentifier" VARCHAR(16777216),
	"TeacherStateID" FLOAT,
	"QuizNumber" FLOAT,
	"ContentLanguage" VARCHAR(16777216),
	"ContentTitle" VARCHAR(16777216),
	"Author" VARCHAR(16777216),
	"FictionNonFiction" VARCHAR(16777216),
	"InterestLevel" VARCHAR(16777216),
	"BookLevel" FLOAT,
	"QuestionsPresented" FLOAT,
	"QuestionsCorrect" FLOAT,
	"PercentCorrect" FLOAT,
	"PointsPossible" FLOAT,
	"PointsEarned" FLOAT,
	"Passed" BOOLEAN,
	TWI VARCHAR(16777216),
	"BookRating" FLOAT,
	"AudioUsed" FLOAT,
	"DateQuizCompleted" VARCHAR(16777216),
	"DateQuizCompletedLocal" VARCHAR(16777216),
	"QuizDeleted" NUMBER(38,0),
	"WordCount" FLOAT,
	"QuizType" VARCHAR(16777216),
	"LexileMeasure" VARCHAR(16777216),
	"LexileLevel" FLOAT
)"""

temp = temp.replace('"', '')
import re
regex = re.compile(r'[\n\t\r]')
temp = regex.sub('', temp)
temp = re.sub('[^a-zA-Z, ]', '', temp)
ts = temp.split(",")
res = {}
from sqlalchemy.types import VARCHAR, FLOAT, NUMERIC
for i in ts:
    x = i.split(" ")
    if len(x)>1:
        if x[1] == "VARCHAR":
            res[str(x[0])] = VARCHAR
        elif x[1] == "FLOAT":
            res[str(x[0])] = FLOAT
        elif x[1] == "NUMBER":
            res[str(x[0])] = NUMERIC
    else:
        print(i)
print(res)


temp1 = temp1.replace('"', '')
temp1 = regex.sub('', temp)
temp1 = re.sub('[^a-zA-Z, ]', '', temp1)
ts = temp1.split(",")
res1 = {}
from sqlalchemy.types import VARCHAR, FLOAT, NUMERIC
for i in ts:
    x = i.split(" ")
    if len(x)>1:
        if x[1] == "VARCHAR":
            res1[str(x[0])] = VARCHAR
        elif x[1] == "FLOAT":
            res1[str(x[0])] = FLOAT
        elif x[1] == "NUMBER":
            res1[str(x[0])] = NUMERIC
    else:
        print(i)
print(res1)
# import pdb;pdb.set_trace()
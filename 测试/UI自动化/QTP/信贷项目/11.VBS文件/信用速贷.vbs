Set qtApp = CreateObject("QuickTest.Application") ' Create the Application object
qtApp.Launch ' Start UFT
qtApp.Visible = True ' Make the UFT application visible
qtApp.ShowPaneScreen "ActiveScreen", True
qtApp.WindowState = "Maximized" 'rem--最大化窗口

' Set UFT run options
qtApp.Options.Run.ImageCaptureForTestResults="OnError"'rem--出错截图

qtApp.Options.Run.RunMode="Fast"'rem--快速运行模式
qtApp.Options.Run.ViewResults=False'rem--运行结束不展示测试报告

qtApp.Open "../01.测试脚本/测试脚本驱动",True 'rem--Open the test in read-only mode只读形式打开测试脚本

Set qtTest = qtApp.Test'rem--set run settings for the test
qtTest.Environment("FileName")="信用速贷流程"
qtTest.Environment("PublicScript")="信用速贷（build）"
qtTest.Settings.Run.IterationMode="rngAll" 'rem--运行时运行所有行
qtTest.Settings.Run.OnError = "Stop" 'rem--'Instruct UFT to Stop when error occurs

Set qtResultsOpt = CreateObject("QuickTest.RunResultsOptions") ' Create the Run Results Options object
qtResultsOpt.ResultsLocation = "..\\09.测试报告\\Res1" ' Set the results location

'Set options for automatic export of run results at the end of every run session

Set qtAutoExportResultsOpts = qtApp.Options.Run.AutoExportReportConfig
qtAutoExportResultsOpts.AutoExportResults = True ' Instruct UFT to automatically export the run results at the end of each run session
qtAutoExportResultsOpts.StepDetailsReport = True ' Instruct UFT to automatically export the step details part of the run results at the end of each run session
qtAutoExportResultsOpts.DataTableReport = True ' Instruct UFT to automatically export the data table part of the run results at the end of each run session
qtAutoExportResultsOpts.LogTrackingReport = True ' Instruct UFT to automatically export the log tracking part of the run results at the end of each run session
qtAutoExportResultsOpts.ScreenRecorderReport = True ' Instruct UFT to automatically export the screen recorder part of the run results at the end of each run session
qtAutoExportResultsOpts.SystemMonitorReport = False ' Instruct UFT not to automatically export the system monitor part of the run results at the end of each run session
qtAutoExportResultsOpts.ExportLocation = "..\\09.测试报告" 'Instruct UFT to automatically export the run results to the Desktop at the end of each run session
qtAutoExportResultsOpts.UserDefinedXSL = "..\\09.测试报告\\MyCustXSL.xsl" ' Specify the customized XSL file when exporting the run results data
qtAutoExportResultsOpts.StepDetailsReportFormat = "UserDefined" ' Instruct UFT to use a customized XSL file when exporting the run results data
qtAutoExportResultsOpts.ExportForFailedRunsOnly = True ' Instruct UFT to automatically export run results only for failed runs

qtTest.Run qtResultsOpt ' Run the test运行测试，报告存储在qtResultsOpt路径

MsgBox qtTest.LastRunResults.Status ' Check the results of the test run
'qtTest.Close ' Close the test

qtApp.quit

Set qtResultsOpt = Nothing ' Release the Run Results Options object
Set qtTest = Nothing ' Release the Test object
Set qtApp = Nothing ' Release the Application object
Set qtAutoExportResultsOpts = Nothing 

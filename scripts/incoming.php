<?php
header('Content-Type: text/html');
?>
<Response>
  <?php if ((strtolower($_REQUEST['Body']) !== 'STOP') && (strtolower($_REQUEST['Body']) !== 'START')) : ?>
  <Message to="<?=$_REQUEST['PhoneNumber']?>">
  <?=htmlspecialchars(substr($_REQUEST['From'] . ": " . $_REQUEST['Body'], 0, 160))?>
  </Message>
  <Message to="<?=$_REQUEST['From']?>">
  Please email info@dubhacks.co with any questions or concerns. Message STOP to opt-out of our announcements.
  </Message>
  <?php endif; ?>
</Response>
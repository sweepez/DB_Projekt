select art.*,
       aut.name
from writtenby as wrt
join author as aut ON wrt.authorid = aut.pid
join article as art ON wrt.articleid = art.aid;

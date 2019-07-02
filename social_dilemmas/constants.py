# Scheme heavily adapted from https://github.com/deepmind/pycolab/
# '@' means "wall"
# 'P' means "player" spawn point
# 'A' means apply spawn point
# '' is empty space

HARVEST_MAP = [
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
    '@ P   P      A    P AAAAA    P  A P  @',
    '@  P     A P AA    P    AAA    A  A  @',
    '@     A AAA  AAA    A    A AA AAAA   @',
    '@ A  AAA A    A  A AAA  A  A   A A   @',
    '@AAA  A A    A  AAA A  AAA        A P@',
    '@ A A  AAA  AAA  A A    A AA   AA AA @',
    '@  A A  AAA    A A  AAA    AAA  A    @',
    '@   AAA  A      AAA  A    AAAA       @',
    '@ P  A       A  A AAA    A  A      P @',
    '@A  AAA  A  A  AAA A    AAAA     P   @',
    '@    A A   AAA  A A      A AA   A  P @',
    '@     AAA   A A  AAA      AA   AAA P @',
    '@ A    A     AAA  A  P          A    @',
    '@       P     A         P  P P     P @',
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@']

HARVEST_MAP_MEDIUM = [
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
    '@ P   P      A    P AAAAA    P @',
    '@  P     A P AA    P    AAA    @',
    '@     A AAA  AAA    A    A AA A@',
    '@ A  AAA A    A  A AAA  A  A   @',
    '@AAA  A A    A  AAA A  AAA     @',
    '@ A A  AAA  AAA  A A    A AA   @',
    '@  A A  AAA    A A  AAA    AAA @',
    '@   AAA  A      AAA  A    AAAA @',
    '@ P  A       A  A AAA    A  A  @',
    '@A  AAA  A  A  AAA A    AAAA   @',
    '@    A A   AAA  A A      A AA  @',
    '@       P     A         P  P P @',
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@']

HARVEST_MAP_SMALL = [
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@',
    '@ P   P      A    P AAAA  P@',
    '@  P     A P A    P    AA  @',
    '@     A AAA  AA    A     A @',
    '@ A  AA A    A  A AAA  A   @',
    '@AAA  A A    A  AA A  AA   @',
    '@ A A  AA  AAA  A A    AA  @',
    '@  A A  AAA    A A  AA   AA@',
    '@   AA  A      AAA  A   AAA@',
    '@ P  A       A  A AA     A @',
    '@    A A   AA  A A       A @',
    '@       P     A        P  P@',
    '@@@@@@@@@@@@@@@@@@@@@@@@@@@@']

HARVEST_MAP_SMALLER = [
    '@@@@@@@@@@@@@@@@@@@@@@',
    '@ P   P      A   P AA@',
    '@  P     A P AA   P  @',
    '@     A AAA  AAA  A  @',
    '@ A  AAA A    A  AAA @',
    '@AAA  A A    A  AAA  @',
    '@ A A  AAA  AAA A A  @',
    '@  A A  AAA   A A  AA@',
    '@ P  A      A  A AAA @',
    '@@@@@@@@@@@@@@@@@@@@@@']

CLEANUP_MAP = [
    '@@@@@@@@@@@@@@@@@@',
    '@RRRRRR     BBBBB@',
    '@HHHHHH      BBBB@',
    '@RRRRRR     BBBBB@',
    '@RRRRR  P    BBBB@',
    '@RRRRR    P BBBBB@',
    '@HHHHH       BBBB@',
    '@RRRRR      BBBBB@',
    '@HHHHHHSSSSSSBBBB@',
    '@HHHHHHSSSSSSBBBB@',
    '@RRRRR   P P BBBB@',
    '@HHHHH   P  BBBBB@',
    '@RRRRRR    P BBBB@',
    '@HHHHHH P   BBBBB@',
    '@RRRRR       BBBB@',
    '@HHHH    P  BBBBB@',
    '@RRRRR       BBBB@',
    '@HHHHH  P P BBBBB@',
    '@RRRRR       BBBB@',
    '@HHHH       BBBBB@',
    '@RRRRR       BBBB@',
    '@HHHHH      BBBBB@',
    '@RRRRR       BBBB@',
    '@HHHH       BBBBB@',
    '@@@@@@@@@@@@@@@@@@']

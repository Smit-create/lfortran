results = [
    ('Module', 'test', [('Declaration', (1, 1), [('decl', 'x', 'integer', [])])], []),
    ('Module', 'test', [('Private', (1, 1), []), ('Declaration', (1, 1), [('decl', 'x', 'integer', [])])], []),
    ('Module', 'test', [('Private', (1, 1), ['x', 'y']), ('Declaration', (1, 1), [('decl', 'x', 'integer', []), ('decl', 'y', 'integer', [])])], []),
    ('Module', 'test', [('Private', (1, 1), ['x', 'y']), ('Declaration', (1, 1), [('decl', 'x', 'integer', []), ('decl', 'y', 'integer', [])])], []),
    ('Module', 'test', [('Public', (1, 1), []), ('Declaration', (1, 1), [('decl', 'x', 'integer', [])])], []),
    ('Module', 'test', [('Public', (1, 1), ['x', 'y']), ('Declaration', (1, 1), [('decl', 'x', 'integer', []), ('decl', 'y', 'integer', [])])], []),
    ('Module', 'test', [('Public', (1, 1), ['x', 'y']), ('Declaration', (1, 1), [('decl', 'x', 'integer', []), ('decl', 'y', 'integer', [])])], []),
    ('Module', 'test', [('Private', (1, 1), []), ('Public', (1, 1), ['x', 'y']), ('Declaration', (1, 1), [('decl', 'x', 'integer', []), ('decl', 'y', 'integer', [])])], []),
    ('Module', 'test', [('Private', (1, 1), ['x']), ('Public', (1, 1), ['y']), ('Declaration', (1, 1), [('decl', 'x', 'integer', []), ('decl', 'y', 'integer', [])])], []),
    ('Module', 'test', [], [('Subroutine', (1, 1), 'a', [('arg', 'b')], [('Declaration', (1, 1), [('decl', 'b', 'integer', [])])], [], [])]),
    ('Module', 'test', [], [('Subroutine', (1, 1), 'a', [('arg', 'b')], [('Declaration', (1, 1), [('decl', 'b', 'integer', [])])], [], []), ('Subroutine', (1, 1), 'f', [('arg', 'b')], [('Declaration', (1, 1), [('decl', 'b', 'integer', [])])], [], [])]),
    ('Module', 'test', [('Declaration', (1, 1), [('decl', 'x', 'integer', [])])], [('Subroutine', (1, 1), 'a', [('arg', 'b')], [('Declaration', (1, 1), [('decl', 'b', 'integer', [])])], [], [])]),
    ('Module', 'test', [], [('Function', (1, 1), 'f', [], None, [], [('Assignment', (1, 1), 'y', ('Num', (1, 1), '0'))], [])]),
    ('Module', 'test', [('Interface', (1, 1), 'name', ['a', 'b', 'c'])], []),
]

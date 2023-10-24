CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; -- UUID 확장 기능 활성화


DROP TABLE IF EXISTS Player CASCADE;
DROP TABLE IF EXISTS alltransaction CASCADE;
DROP TYPE IF EXISTS txtype CASCADE;
DROP TABLE IF EXISTS gameinfo CASCADE;
DROP TABLE IF EXISTS ResultOfPlayer CASCADE;

-- 1. 플레이어table
CREATE TABLE Player (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    nickname TEXT NOT NULL,
    totalbuyin NUMERIC NOT NULL,
    totalout NUMERIC NOT NULL,
    netscore NUMERIC NOT NULL,
    noofgames INTEGER NOT NULL,
    getbbozziratio NUMERIC NOT NULL,
    setbbozziratio NUMERIC NOT NULL
);

-- 2. 트랜젝션table
CREATE TYPE TxType AS ENUM ('buyin', 'endchip', 'setbbozzi', 'getbbozzi', 'gamefee'); -- enum type 생성

CREATE TABLE AllTransaction (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    playerid UUID REFERENCES Player(id),
    transactiontype TxType NOT NULL,
    amount NUMERIC NOT NULL,
    time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 3. 게임table
CREATE TABLE GameInfo (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    netPlayer INTEGER NOT NULL,
    netbuyin NUMERIC NOT NULL,
    netgamefee NUMERIC NOT NULL,
    netbbozzi NUMERIC NOT NULL,
    start TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    finish TIMESTAMP NOT NULL,
    playtimemin INTEGER NOT NULL
);

-- 4. 결과table
CREATE TABLE ResultOfPlayer (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    gameinfoid UUID NOT NULL REFERENCES GameInfo(id),
    playerid UUID NOT NULL REFERENCES Player(id),
    buyin NUMERIC NOT NULL,
    chipout NUMERIC NOT NULL,
    actualresult NUMERIC NOT NULL,
    rankongame INTEGER NOT NULL
);

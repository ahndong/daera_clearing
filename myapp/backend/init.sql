CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; -- UUID 확장 기능 활성화


DROP TABLE IF EXISTS Player CASCADE;
DROP TABLE IF EXISTS alltransaction CASCADE;
DROP TYPE IF EXISTS txtype CASCADE;
DROP TABLE IF EXISTS gameinfo CASCADE;
DROP TABLE IF EXISTS ResultOfPlayer CASCADE;

-- 1. 플레이어table
CREATE TABLE Player (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    nickName TEXT NOT NULL,
    totalBuyin NUMERIC NOT NULL,
    totalOut NUMERIC NOT NULL,
    netScore NUMERIC NOT NULL,
    noOfGames INTEGER NOT NULL,
    getBbozziRatio NUMERIC NOT NULL,
    setBbozziRatio NUMERIC NOT NULL
);

-- 2. 트랜젝션table
CREATE TYPE TxType AS ENUM ('buyin', 'endchip', 'setbbozzi', 'getbbozzi', 'gamefee'); -- enum type 생성

CREATE TABLE AllTransaction (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    playerId UUID REFERENCES Player(id),
    transactionType TxType NOT NULL,
    amount NUMERIC NOT NULL,
    time TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 3. 게임table
CREATE TABLE GameInfo (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    netPlayer INTEGER NOT NULL,
    netBuyin NUMERIC NOT NULL,
    netGameFee NUMERIC NOT NULL,
    netBbozzi NUMERIC NOT NULL,
    start TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    finish TIMESTAMP NOT NULL,
    playTimeMin INTEGER NOT NULL
);

-- 4. 결과table
CREATE TABLE ResultOfPlayer (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    gameInfoId UUID NOT NULL REFERENCES GameInfo(id),
    playerId UUID NOT NULL REFERENCES Player(id),
    buyIn NUMERIC NOT NULL,
    chipOut NUMERIC NOT NULL,
    actualResult NUMERIC NOT NULL,
    rankOnGame INTEGER NOT NULL
);

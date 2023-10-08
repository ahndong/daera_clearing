CREATE EXTENSION IF NOT EXISTS "uuid-ossp"; -- UUID 확장 기능 활성화

-- 1. 플레이어table
CREATE TABLE Player (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    이름 TEXT NOT NULL,
    totalBuyin NUMERIC NOT NULL,
    totalOut NUMERIC NOT NULL,
    netScore NUMERIC NOT NULL,
    noOfGames INTEGER NOT NULL,
    getBbozziRatio NUMERIC NOT NULL,
    setBbozziRatio NUMERIC NOT NULL
);

-- 2. 트랜젝션table
CREATE TYPE TrType AS ENUM ('buyin', 'endchip', 'setbbozzi', 'getbbozzi', 'gamefee'); -- enum type 생성

CREATE TABLE Transaction (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    trType TrType NOT NULL,
    amount NUMERIC NOT NULL,
    time TIMESTAMP NOT NULL
);

-- 3. 게임table
CREATE TABLE Game (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    netPlayer INTEGER NOT NULL,
    netBuyin NUMERIC NOT NULL,
    netGameFee NUMERIC NOT NULL,
    netBbozzi NUMERIC NOT NULL,
    start TIMESTAMP NOT NULL,
    end TIMESTAMP NOT NULL,
    playTimeMin INTEGER NOT NULL
);

-- 4. 결과table
CREATE TABLE Result (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    gameId UUID REFERENCES Game(id), -- foreign key 설정
    playerId UUID REFERENCES Player(id), -- foreign key 설정
    buyin NUMERIC NOT NULL,
    result NUMERIC NOT NULL,
    rank INTEGER NOT NULL
);

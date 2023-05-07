-- Table: public.t_power

-- DROP TABLE IF EXISTS public.t_power;

CREATE TABLE IF NOT EXISTS public.t_power
(
    power double precision NOT NULL,
    daily_yield double precision NOT NULL,
    total_yield double precision NOT NULL,
    created_at timestamp with time zone NOT NULL DEFAULT now(),
    CONSTRAINT t_power_pkey PRIMARY KEY (created_at)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.t_power
    OWNER to postgres;

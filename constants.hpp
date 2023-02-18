#ifndef CONSTANTS_HPP
#define CONSTANTS_HPP

struct Area_Arguments {
    // 评估区域中环境和经济的权重，即计算中的α。该数值应在0到1之间。
    double env_eco_rate;
    // 面积
    double S;
};

extern Area_Arguments mara_triangle, musiara_sector, sekenani_sector;

#endif
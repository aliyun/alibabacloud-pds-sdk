// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class PunishmentResponse extends TeaModel {
    @NameInMap("ends_at")
    public String endsAt;

    /**
     * <p>ActionCode  string `json:"action_code,omitempty"` // 无需求暂不提供</p>
     */
    @NameInMap("impermanent")
    public Boolean impermanent;

    @NameInMap("punish_flag")
    public Long punishFlag;

    @NameInMap("starts_at")
    public String startsAt;

    public static PunishmentResponse build(java.util.Map<String, ?> map) throws Exception {
        PunishmentResponse self = new PunishmentResponse();
        return TeaModel.build(map, self);
    }

    public PunishmentResponse setEndsAt(String endsAt) {
        this.endsAt = endsAt;
        return this;
    }
    public String getEndsAt() {
        return this.endsAt;
    }

    public PunishmentResponse setImpermanent(Boolean impermanent) {
        this.impermanent = impermanent;
        return this;
    }
    public Boolean getImpermanent() {
        return this.impermanent;
    }

    public PunishmentResponse setPunishFlag(Long punishFlag) {
        this.punishFlag = punishFlag;
        return this;
    }
    public Long getPunishFlag() {
        return this.punishFlag;
    }

    public PunishmentResponse setStartsAt(String startsAt) {
        this.startsAt = startsAt;
        return this;
    }
    public String getStartsAt() {
        return this.startsAt;
    }

}

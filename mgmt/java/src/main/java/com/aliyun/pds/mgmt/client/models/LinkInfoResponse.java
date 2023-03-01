// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class LinkInfoResponse extends TeaModel {
    /**
     * <p>认证类型</p>
     */
    @NameInMap("authentication_type")
    @Validation(required = true)
    public String authenticationType;

    /**
     * <p>创建时间</p>
     */
    @NameInMap("created_at")
    @Validation(required = true)
    public Long createdAt;

    /**
     * <p>显示名称</p>
     */
    @NameInMap("display_name")
    @Validation(required = true)
    public String displayName;

    /**
     * <p>Domain ID</p>
     */
    @NameInMap("domain_id")
    @Validation(required = true)
    public String domainId;

    /**
     * <p>额外的信息，比如type为mobile时，此字段为国家编号，不填默认86</p>
     */
    @NameInMap("extra")
    public String extra;

    /**
     * <p>唯一身份标识</p>
     */
    @NameInMap("identity")
    @Validation(required = true)
    public String identity;

    /**
     * <p>最后登录时间</p>
     */
    @NameInMap("last_login_time")
    @Validation(required = true)
    public Long lastLoginTime;

    /**
     * <p>状态</p>
     */
    @NameInMap("status")
    @Validation(required = true)
    public String status;

    /**
     * <p>用户ID</p>
     */
    @NameInMap("user_id")
    @Validation(required = true)
    public String userId;

    public static LinkInfoResponse build(java.util.Map<String, ?> map) throws Exception {
        LinkInfoResponse self = new LinkInfoResponse();
        return TeaModel.build(map, self);
    }

    public LinkInfoResponse setAuthenticationType(String authenticationType) {
        this.authenticationType = authenticationType;
        return this;
    }
    public String getAuthenticationType() {
        return this.authenticationType;
    }

    public LinkInfoResponse setCreatedAt(Long createdAt) {
        this.createdAt = createdAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.createdAt;
    }

    public LinkInfoResponse setDisplayName(String displayName) {
        this.displayName = displayName;
        return this;
    }
    public String getDisplayName() {
        return this.displayName;
    }

    public LinkInfoResponse setDomainId(String domainId) {
        this.domainId = domainId;
        return this;
    }
    public String getDomainId() {
        return this.domainId;
    }

    public LinkInfoResponse setExtra(String extra) {
        this.extra = extra;
        return this;
    }
    public String getExtra() {
        return this.extra;
    }

    public LinkInfoResponse setIdentity(String identity) {
        this.identity = identity;
        return this;
    }
    public String getIdentity() {
        return this.identity;
    }

    public LinkInfoResponse setLastLoginTime(Long lastLoginTime) {
        this.lastLoginTime = lastLoginTime;
        return this;
    }
    public Long getLastLoginTime() {
        return this.lastLoginTime;
    }

    public LinkInfoResponse setStatus(String status) {
        this.status = status;
        return this;
    }
    public String getStatus() {
        return this.status;
    }

    public LinkInfoResponse setUserId(String userId) {
        this.userId = userId;
        return this;
    }
    public String getUserId() {
        return this.userId;
    }

}

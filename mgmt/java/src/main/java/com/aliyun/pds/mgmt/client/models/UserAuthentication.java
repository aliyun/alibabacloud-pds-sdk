// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.mgmt.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UserAuthentication extends TeaModel {
    /**
     * <p>认证类型</p>
     */
    @NameInMap("AuthenticationType")
    @Validation(required = true)
    public String AuthenticationType;

    /**
     * <p>创建时间</p>
     */
    @NameInMap("CreatedAt")
    @Validation(required = true)
    public Long CreatedAt;

    /**
     * <p>详情</p>
     */
    @NameInMap("Detail")
    @Validation(required = true)
    public String Detail;

    /**
     * <p>Domain ID</p>
     */
    @NameInMap("DomainID")
    @Validation(required = true)
    public String DomainID;

    /**
     * <p>额外的信息，比如type为mobile时，此字段为国家编号，不填默认86</p>
     */
    @NameInMap("Extra")
    public String Extra;

    /**
     * <p>唯一身份标识</p>
     */
    @NameInMap("Identity")
    @Validation(required = true)
    public String Identity;

    /**
     * <p>最后登录时间</p>
     */
    @NameInMap("LastLoginTime")
    @Validation(required = true)
    public Long LastLoginTime;

    /**
     * <p>状态</p>
     */
    @NameInMap("Status")
    @Validation(required = true)
    public String Status;

    /**
     * <p>用户ID</p>
     */
    @NameInMap("UserID")
    @Validation(required = true)
    public String UserID;

    /**
     * <p>subdomain id</p>
     */
    @NameInMap("subdomain_id")
    public String subdomainId;

    public static UserAuthentication build(java.util.Map<String, ?> map) throws Exception {
        UserAuthentication self = new UserAuthentication();
        return TeaModel.build(map, self);
    }

    public UserAuthentication setAuthenticationType(String AuthenticationType) {
        this.AuthenticationType = AuthenticationType;
        return this;
    }
    public String getAuthenticationType() {
        return this.AuthenticationType;
    }

    public UserAuthentication setCreatedAt(Long CreatedAt) {
        this.CreatedAt = CreatedAt;
        return this;
    }
    public Long getCreatedAt() {
        return this.CreatedAt;
    }

    public UserAuthentication setDetail(String Detail) {
        this.Detail = Detail;
        return this;
    }
    public String getDetail() {
        return this.Detail;
    }

    public UserAuthentication setDomainID(String DomainID) {
        this.DomainID = DomainID;
        return this;
    }
    public String getDomainID() {
        return this.DomainID;
    }

    public UserAuthentication setExtra(String Extra) {
        this.Extra = Extra;
        return this;
    }
    public String getExtra() {
        return this.Extra;
    }

    public UserAuthentication setIdentity(String Identity) {
        this.Identity = Identity;
        return this;
    }
    public String getIdentity() {
        return this.Identity;
    }

    public UserAuthentication setLastLoginTime(Long LastLoginTime) {
        this.LastLoginTime = LastLoginTime;
        return this;
    }
    public Long getLastLoginTime() {
        return this.LastLoginTime;
    }

    public UserAuthentication setStatus(String Status) {
        this.Status = Status;
        return this;
    }
    public String getStatus() {
        return this.Status;
    }

    public UserAuthentication setUserID(String UserID) {
        this.UserID = UserID;
        return this;
    }
    public String getUserID() {
        return this.UserID;
    }

    public UserAuthentication setSubdomainId(String subdomainId) {
        this.subdomainId = subdomainId;
        return this;
    }
    public String getSubdomainId() {
        return this.subdomainId;
    }

}

// This file is auto-generated, don't edit it. Thanks.
package com.aliyun.pds.client.models;

import com.aliyun.tea.*;

/**
 * 
 */
public class UserAuthentication extends TeaModel {
    // 认证类型
    @NameInMap("AuthenticationType")
    @Validation(required = true)
    public String AuthenticationType;

    // 创建时间
    @NameInMap("CreatedAt")
    @Validation(required = true)
    public Long CreatedAt;

    // 详情
    @NameInMap("Detail")
    @Validation(required = true)
    public String Detail;

    // Domain ID
    @NameInMap("DomainID")
    @Validation(required = true)
    public String DomainID;

    // 唯一身份标识
    @NameInMap("Identity")
    @Validation(required = true)
    public String Identity;

    // 最后登录时间
    @NameInMap("LastLoginTime")
    @Validation(required = true)
    public Long LastLoginTime;

    // 状态
    @NameInMap("Status")
    @Validation(required = true)
    public String Status;

    // 用户ID
    @NameInMap("UserID")
    @Validation(required = true)
    public String UserID;

    // 额外的信息，比如type为mobile时，此字段为国家编号，不填默认86
    @NameInMap("extra")
    public String extra;

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

    public UserAuthentication setExtra(String extra) {
        this.extra = extra;
        return this;
    }
    public String getExtra() {
        return this.extra;
    }

}

// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 
     */
    public class GetAppResponse : TeaModel {
        /// <summary>
        /// App 拥有者
        /// </summary>
        [NameInMap("ali_owner_id")]
        [Validation(Required=true)]
        public string AliOwnerId { get; set; }

        /// <summary>
        /// App ID
        /// </summary>
        [NameInMap("app_id")]
        [Validation(Required=true)]
        public string AppId { get; set; }

        /// <summary>
        /// App名称
        /// </summary>
        [NameInMap("app_name")]
        [Validation(Required=true, MaxLength=128, Pattern="[0-9a-zA-Z]+")]
        public string AppName { get; set; }

        /// <summary>
        /// App 秘钥
        /// </summary>
        [NameInMap("app_secret")]
        [Validation(Required=true)]
        public string AppSecret { get; set; }

        /// <summary>
        /// App 创建时间
        /// </summary>
        [NameInMap("created_at")]
        [Validation(Required=true)]
        public string CreatedAt { get; set; }

        /// <summary>
        /// App描述
        /// </summary>
        [NameInMap("description")]
        [Validation(Required=true, MaxLength=128)]
        public string Description { get; set; }

        /// <summary>
        /// App图标
        /// </summary>
        [NameInMap("logo")]
        [Validation(Required=true)]
        public string Logo { get; set; }

        /// <summary>
        /// App 提供方
        /// </summary>
        [NameInMap("provider")]
        [Validation(Required=true)]
        public string Provider { get; set; }

        /// <summary>
        /// App回调地址
        /// </summary>
        [NameInMap("redirect_uri")]
        [Validation(Required=true)]
        public string RedirectUri { get; set; }

        /// <summary>
        /// App权限列表
        /// </summary>
        [NameInMap("scope")]
        [Validation(Required=true)]
        public List<string> Scope { get; set; }

        /// <summary>
        /// App 屏幕截图
        /// </summary>
        [NameInMap("screenshots")]
        [Validation(Required=true)]
        public List<string> Screenshots { get; set; }

        /// <summary>
        /// App 当前阶段
        /// </summary>
        [NameInMap("stage")]
        [Validation(Required=true)]
        public string Stage { get; set; }

        /// <summary>
        /// App类型
        /// </summary>
        [NameInMap("type")]
        [Validation(Required=true)]
        public string Type { get; set; }

        /// <summary>
        /// App 修改时间
        /// </summary>
        [NameInMap("updated_at")]
        [Validation(Required=true)]
        public string UpdatedAt { get; set; }

    }

}

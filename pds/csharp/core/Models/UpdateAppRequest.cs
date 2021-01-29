// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 
     */
    public class UpdateAppRequest : TeaModel {
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
        [Validation(Required=false, MaxLength=128)]
        public string AppName { get; set; }

        /// <summary>
        /// App描述
        /// </summary>
        [NameInMap("description")]
        [Validation(Required=false, MaxLength=1024)]
        public string Description { get; set; }

        /// <summary>
        /// App图标
        /// </summary>
        [NameInMap("logo")]
        [Validation(Required=false)]
        public string Logo { get; set; }

        /// <summary>
        /// App回调地址
        /// </summary>
        [NameInMap("redirect_uri")]
        [Validation(Required=false)]
        public string RedirectUri { get; set; }

        /// <summary>
        /// App权限列表
        /// </summary>
        [NameInMap("scope")]
        [Validation(Required=false)]
        public List<string> Scope { get; set; }

        /// <summary>
        /// App类型
        /// </summary>
        [NameInMap("type")]
        [Validation(Required=false)]
        public string Type { get; set; }

    }

}

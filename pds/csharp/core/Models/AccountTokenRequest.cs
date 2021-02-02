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
    public class AccountTokenRequest : TeaModel {
        [NameInMap("headers")]
        [Validation(Required=false)]
        public Dictionary<string, string> Headers { get; set; }

        /// <summary>
        /// addition_data
        /// </summary>
        [NameInMap("addition_data")]
        [Validation(Required=false)]
        public Dictionary<string, object> AdditionData { get; set; }

        /// <summary>
        /// App ID, 当前访问的App
        /// </summary>
        [NameInMap("app_id")]
        [Validation(Required=true)]
        public string AppId { get; set; }

        /// <summary>
        /// 只能填refresh_token
        /// </summary>
        [NameInMap("grant_type")]
        [Validation(Required=true)]
        public string GrantType { get; set; }

        /// <summary>
        /// refresh token, 登录时返回的
        /// </summary>
        [NameInMap("refresh_token")]
        [Validation(Required=true)]
        public string RefreshToken { get; set; }

    }

}

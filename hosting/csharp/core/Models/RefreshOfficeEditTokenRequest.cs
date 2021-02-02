// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.Hosting.Client.Models
{
    /**
     * 刷新office文档在线编辑凭证
     */
    public class RefreshOfficeEditTokenRequest : TeaModel {
        /// <summary>
        /// addition_data
        /// </summary>
        [NameInMap("addition_data")]
        [Validation(Required=false)]
        public Dictionary<string, object> AdditionData { get; set; }

        /// <summary>
        /// location
        /// </summary>
        [NameInMap("location")]
        [Validation(Required=false)]
        public string Location { get; set; }

        /// <summary>
        /// AccessToken
        /// </summary>
        [NameInMap("office_access_token")]
        [Validation(Required=true)]
        public string OfficeAccessToken { get; set; }

        /// <summary>
        /// RefreshToken
        /// </summary>
        [NameInMap("office_refresh_token")]
        [Validation(Required=true)]
        public string OfficeRefreshToken { get; set; }

    }

}

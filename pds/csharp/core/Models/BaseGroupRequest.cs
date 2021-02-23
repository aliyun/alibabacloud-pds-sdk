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
    public class BaseGroupRequest : TeaModel {
        /// <summary>
        /// 描述
        /// </summary>
        [NameInMap("description")]
        [Validation(Required=false)]
        public string Description { get; set; }

        /// <summary>
        /// 名称
        /// </summary>
        [NameInMap("group_name")]
        [Validation(Required=true)]
        public string GroupName { get; set; }

        /// <summary>
        /// 是否是根group
        /// </summary>
        [NameInMap("is_root")]
        [Validation(Required=false)]
        public bool? IsRoot { get; set; }

    }

}

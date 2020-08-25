// This file is auto-generated, don't edit it. Thanks.

using System;
using System.Collections.Generic;
using System.IO;

using Tea;

namespace Aliyun.SDK.PDS.Client.Models
{
    /**
     * 批量删除文件 response
     */
    public class OSSDeleteFilesResponse : TeaModel {
        /// <summary>
        /// deleted_file_id_list
        /// </summary>
        [NameInMap("deleted_file_id_list")]
        [Validation(Required=false)]
        public List<string> DeletedFileIdList { get; set; }

        /// <summary>
        /// domain_id
        /// </summary>
        [NameInMap("domain_id")]
        [Validation(Required=false, Pattern="[a-z0-9A-Z]+")]
        public string DomainId { get; set; }

        /// <summary>
        /// drive_id
        /// </summary>
        [NameInMap("drive_id")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public string DriveId { get; set; }

        /// <summary>
        /// share_id
        /// </summary>
        [NameInMap("share_id")]
        [Validation(Required=false, Pattern="[0-9]+")]
        public string ShareId { get; set; }

    }

}

<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

/**
 * 获取视频DRM License.
 */
class OSSVideoDRMLicenseRequest extends Model
{
    /**
     * @description drmType
     *
     * @example widevine,fairplay
     *
     * @var string
     */
    public $drmType;

    /**
     * @description licenseRequest
     *
     * @example xxx
     *
     * @var string
     */
    public $licenseRequest;
    protected $_name = [
        'drmType'        => 'drmType',
        'licenseRequest' => 'licenseRequest',
    ];

    public function validate()
    {
        Model::validateRequired('drmType', $this->drmType, true);
        Model::validateRequired('licenseRequest', $this->licenseRequest, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->drmType) {
            $res['drmType'] = $this->drmType;
        }
        if (null !== $this->licenseRequest) {
            $res['licenseRequest'] = $this->licenseRequest;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return OSSVideoDRMLicenseRequest
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['drmType'])) {
            $model->drmType = $map['drmType'];
        }
        if (isset($map['licenseRequest'])) {
            $model->licenseRequest = $map['licenseRequest'];
        }

        return $model;
    }
}

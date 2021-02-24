<?php

// This file is auto-generated, don't edit it. Thanks.

namespace Aliyun\PDS\SDK\Models;

use AlibabaCloud\Tea\Model;

class CertInfo extends Model
{
    /**
     * @var string
     */
    public $CertID;

    /**
     * @description cert body
     *
     * @example xxxxxxxxxxx
     *
     * @var string
     */
    public $certBody;

    /**
     * @description cert name
     *
     * @example mysite2020cert
     *
     * @var string
     */
    public $certName;

    /**
     * @description cert privatekey
     *
     * @example yyyyyyyyyy
     *
     * @var string
     */
    public $certPrivatekey;
    protected $_name = [
        'CertID'         => 'CertID',
        'certBody'       => 'cert_body',
        'certName'       => 'cert_name',
        'certPrivatekey' => 'cert_privatekey',
    ];

    public function validate()
    {
        Model::validateRequired('certBody', $this->certBody, true);
        Model::validateRequired('certName', $this->certName, true);
        Model::validateRequired('certPrivatekey', $this->certPrivatekey, true);
    }

    public function toMap()
    {
        $res = [];
        if (null !== $this->CertID) {
            $res['CertID'] = $this->CertID;
        }
        if (null !== $this->certBody) {
            $res['cert_body'] = $this->certBody;
        }
        if (null !== $this->certName) {
            $res['cert_name'] = $this->certName;
        }
        if (null !== $this->certPrivatekey) {
            $res['cert_privatekey'] = $this->certPrivatekey;
        }

        return $res;
    }

    /**
     * @param array $map
     *
     * @return CertInfo
     */
    public static function fromMap($map = [])
    {
        $model = new self();
        if (isset($map['CertID'])) {
            $model->CertID = $map['CertID'];
        }
        if (isset($map['cert_body'])) {
            $model->certBody = $map['cert_body'];
        }
        if (isset($map['cert_name'])) {
            $model->certName = $map['cert_name'];
        }
        if (isset($map['cert_privatekey'])) {
            $model->certPrivatekey = $map['cert_privatekey'];
        }

        return $model;
    }
}
